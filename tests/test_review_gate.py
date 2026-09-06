import copy
from datetime import date
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from review_gate import evaluate, freshness, reconcile
from import_taxonomy import parse_taxonomy

TODAY = date(2026, 9, 5)

def valid_context():
    return {"country": "Canada", "province": "Ontario", "activity": "records-review", "site_area": "records-room",
            "licence": {"evidence_id": "FICTIONAL-LIC-01", "conditions_reviewed": True, "valid_from": "2026-01-01", "valid_to": "2026-12-31",
                        "authorized_activities": ["records-review"], "authorized_areas": ["records-room"]},
            "role": {"name": "Fictional quality reviewer", "appointment_evidence": "FICTIONAL-ROLE-01"},
            "sources": [{"last_verified": "2026-09-05", "freshness_interval": 30}], "evidence": ["FICTIONAL-RECORD-01"]}

class GateTests(unittest.TestCase):
    def test_complete_evidence_never_becomes_authorization(self):
        result = evaluate(valid_context(), TODAY)
        self.assertEqual(result["status"], "REVIEW_SUPPORT_ONLY")
        self.assertFalse(result["human_authorization"])

    def test_missing_licence_allows_only_gap_review(self):
        c = valid_context(); del c["licence"]
        self.assertEqual(evaluate(c, TODAY)["status"], "MORE_EVIDENCE_REQUIRED")

    def test_wrong_activity_and_area_independently_fail(self):
        for key in ("activity", "site_area"):
            c = valid_context(); c[key] = "outside-supplied-authority"
            self.assertEqual(evaluate(c, TODAY)["status"], "OUTSIDE_DOCUMENTED_AUTHORITY")

    def test_expired_or_unverified_licence(self):
        for key, value in (("valid_to", "2026-08-01"), ("valid_from", "invalid"), ("conditions_reviewed", False)):
            c = valid_context(); c["licence"][key] = value
            self.assertEqual(evaluate(c, TODAY)["status"], "MORE_EVIDENCE_REQUIRED")

    def test_wrong_country_and_missing_province(self):
        c = valid_context(); c["country"] = "United States"
        self.assertEqual(evaluate(c, TODAY)["status"], "MORE_EVIDENCE_REQUIRED")
        c = valid_context(); c["provincial_required"] = True; del c["province"]
        self.assertIn("Missing provincial jurisdiction", evaluate(c, TODAY)["issues"])

    def test_role_title_without_appointment_is_insufficient(self):
        c = valid_context(); del c["role"]["appointment_evidence"]
        self.assertEqual(evaluate(c, TODAY)["status"], "MORE_EVIDENCE_REQUIRED")

    def test_missing_evidence_and_unsupported_assumptions(self):
        c = valid_context(); c["evidence"] = []; c["unsupported_assumptions"] = ["COA represents every lot"]
        self.assertEqual(len(evaluate(c, TODAY)["issues"]), 2)

    def test_stale_missing_future_and_superseded_sources(self):
        for s in ({}, {"last_verified": "2026-07-01", "freshness_interval": 30},
                  {"last_verified": "2027-01-01", "freshness_interval": 30},
                  {"last_verified": "2026-09-05", "freshness_interval": 30, "superseded": True}):
            self.assertEqual(freshness(s, TODAY), "REVERIFICATION_REQUIRED")

    def test_access_date_does_not_hide_consolidation_gap(self):
        s = {"last_verified": "2026-09-05", "freshness_interval": 30, "current_to": "2026-06-21"}
        self.assertEqual(freshness(s, TODAY), "REVERIFICATION_REQUIRED")

    def test_human_actions_and_engineering_do_not_pass(self):
        for action in ("release-lot", "submit-report", "remove-hold", "approve-recall", "approve-engineering"):
            c = valid_context(); c["requested_action"] = action
            self.assertEqual(evaluate(c, TODAY)["status"], "QUALIFIED_REVIEW_REQUIRED")
        c = valid_context(); c["hazard_class"] = "ENGINEERING_BOUNDARY"
        self.assertEqual(evaluate(c, TODAY)["status"], "QUALIFIED_REVIEW_REQUIRED")

    def test_boundary_overrides_supplied_licence_and_routine_hazard(self):
        for action in ("operate-extraction", "configure-pressure", "bypass-interlock", "optimize-potency", "grow-production-protocol",
                       "falsify-record", "conceal-test", "manipulate-ctls", "unapproved-pesticide-use"):
            c = valid_context(); c["requested_action"] = action; c["hazard_class"] = "ROUTINE_PROCESS"
            self.assertEqual(evaluate(c, TODAY)["status"], "BOUNDARY_REDIRECTION")

    def test_decimal_inventory_conservation(self):
        r = reconcile("0.1", "0.2", "0", "0.3", units=["kg"] * 4)
        self.assertEqual(r["status"], "RECONCILED")
        r = reconcile(100, 20, 15, 104, units=["kg"] * 4)
        self.assertEqual(r["difference"], "-1")

    def test_invalid_inventory_cannot_be_silently_repaired(self):
        for args in ((0, 1, 3, 0), ("NaN", 1, 0, 1), (-1, 1, 0, 0)):
            with self.assertRaises(ValueError): reconcile(*args, units=["kg"] * 4)
        with self.assertRaises(ValueError): reconcile(1, 1, 0, 2, units=["kg", "g", "kg", "kg"])

    def test_taxonomy_annotations_do_not_change_authority(self):
        root = Path(__file__).resolve().parents[1]
        families = parse_taxonomy((root / "docs/development/taxonomy-source.md").read_text(encoding="utf-8-sig"))
        names = [n for f in families for n in f["skills"]]
        self.assertEqual(len(names), 233)
        self.assertEqual(len(set(names)), 233)
        self.assertNotIn("audit-production-batch-record", names)
        self.assertEqual(names.count("build-product-stability-program"), 1)

if __name__ == "__main__": unittest.main()
