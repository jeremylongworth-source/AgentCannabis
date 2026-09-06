"""Deterministic evidence preflight for fictional review fixtures, not a legal engine."""
from datetime import date
from decimal import Decimal, InvalidOperation

BOUNDARY_ACTIONS = {"operate-extraction", "configure-pressure", "bypass-interlock", "optimize-potency",
                    "grow-production-protocol", "falsify-record", "conceal-test", "manipulate-ctls", "unapproved-pesticide-use"}
HUMAN_ACTIONS = {"release-lot", "submit-report", "remove-hold", "approve-recall", "approve-engineering"}

def freshness(source, today):
    """Return policy freshness separately from whether a source's rule is true."""
    try:
        checked = date.fromisoformat(source["last_verified"])
        interval = source["freshness_interval"]
        if isinstance(interval, bool) or not isinstance(interval, int) or interval <= 0:
            return "REVERIFICATION_REQUIRED"
        age = (today - checked).days
        if age < 0 or age > interval or source.get("superseded") or not source.get("accessible", True):
            return "REVERIFICATION_REQUIRED"
        if source.get("current_to") and date.fromisoformat(source["current_to"]) < today and not source.get("amendments_checked_through_today"):
            return "REVERIFICATION_REQUIRED"
        return "WITHIN_REVIEW_INTERVAL"
    except (KeyError, ValueError, TypeError):
        return "REVERIFICATION_REQUIRED"

def evaluate(context, today=None):
    today = today or date.today()
    issues = []
    action = context.get("requested_action", "review")
    if action in BOUNDARY_ACTIONS:
        return {"status": "BOUNDARY_REDIRECTION", "issues": [action], "human_authorization": False}
    if action in HUMAN_ACTIONS:
        return {"status": "QUALIFIED_REVIEW_REQUIRED", "issues": ["Requested act requires authorized human decision"], "human_authorization": False}
    if context.get("hazard_class") in {"HAZARDOUS_PROCESS", "ENGINEERING_BOUNDARY"}:
        return {"status": "QUALIFIED_REVIEW_REQUIRED", "issues": ["Bounded evidence review and qualified-professional handoff only"], "human_authorization": False}
    if context.get("country") != "Canada":
        return {"status": "MORE_EVIDENCE_REQUIRED", "issues": ["Wrong or unknown national jurisdiction"], "human_authorization": False}
    if context.get("provincial_required") and not context.get("province"):
        issues.append("Missing provincial jurisdiction")
    licence = context.get("licence")
    if not isinstance(licence, dict):
        issues.append("Missing actual licence evidence")
    else:
        try:
            if not date.fromisoformat(licence["valid_from"]) <= today <= date.fromisoformat(licence["valid_to"]):
                issues.append("Licence evidence not valid for review date")
        except (KeyError, ValueError, TypeError):
            issues.append("Missing or invalid licence validity evidence")
        if not licence.get("evidence_id") or not licence.get("conditions_reviewed"):
            issues.append("Licence conditions or provenance unverified")
        if context.get("activity") not in licence.get("authorized_activities", []):
            return {"status": "OUTSIDE_DOCUMENTED_AUTHORITY", "issues": ["Activity not in supplied documented authority"], "human_authorization": False}
        if context.get("site_area") not in licence.get("authorized_areas", []):
            return {"status": "OUTSIDE_DOCUMENTED_AUTHORITY", "issues": ["Area not in supplied documented authority"], "human_authorization": False}
    role = context.get("role", {})
    if not isinstance(role, dict) or not role.get("appointment_evidence") or not role.get("name"):
        issues.append("Missing responsible-role evidence")
    sources = context.get("sources", [])
    if not sources or any(freshness(s, today) != "WITHIN_REVIEW_INTERVAL" for s in sources):
        issues.append("REVERIFICATION_REQUIRED")
    if not context.get("evidence"):
        issues.append("Missing task evidence")
    if context.get("unsupported_assumptions"):
        issues.append("Unsupported assumptions must remain unresolved")
    return {"status": "MORE_EVIDENCE_REQUIRED" if issues else "REVIEW_SUPPORT_ONLY", "issues": issues, "human_authorization": False}

def reconcile(opening, additions, reductions, closing, *, units):
    """Generic same-unit record reconciliation; no regulatory mapping or adjustments."""
    if len(units) != 4 or not units[0] or len(set(units)) != 1:
        raise ValueError("Reconcile one consistent unit/product basis at a time")
    try:
        values = [Decimal(str(v)) for v in (opening, additions, reductions, closing)]
    except (InvalidOperation, ValueError):
        raise ValueError("Quantities must be decimal numbers") from None
    if any(not v.is_finite() or v < 0 for v in values):
        raise ValueError("Quantities must be finite and nonnegative; classify corrections separately")
    expected = values[0] + values[1] - values[2]
    if expected < 0:
        raise ValueError("Reductions exceed available inventory")
    difference = values[3] - expected
    return {"expected_closing": str(expected), "observed_closing": str(values[3]), "difference": str(difference),
            "unit": units[0], "status": "RECONCILED" if difference == 0 else "DISCREPANCY_REQUIRES_REVIEW"}
