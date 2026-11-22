
import pytest

from app.schemas.alert import Alert, Severity, AlertStatus
from app.schemas.evidence import Evidence, EvidenceType
from app.schemas.incident import Incident


def test_create_alert():
    alert = Alert(
        title="Suspicious Login",
        description="Multiple failed logins followed by success",
        source="Microsoft Sentinel",
        severity="high"
    )

    assert alert.severity == Severity.HIGH
    assert alert.status == AlertStatus.NEW
    assert alert.id is not None


def test_invalid_severity():
    with pytest.raises(ValueError):
        Alert(
            title="Suspicious Login",
            description="Test alert",
            source="Sentinel",
            severity="super-dangerous"
        )


def test_create_evidence():
    alert = Alert(
        title="Suspicious Login",
        description="Unusual authentication activity",
        source="Sentinel",
        severity="high"
    )

    evidence = Evidence(
        alert_id=alert.id,
        evidence_type="identity",
        source="Microsoft Sentinel",
        description="Five failed login attempts"
    )

    assert evidence.alert_id == alert.id
    assert evidence.evidence_type == EvidenceType.IDENTITY


def test_create_incident():
    alert = Alert(
        title="Suspicious Login",
        description="Unusual authentication",
        source="Sentinel",
        severity="high"
    )

    incident = Incident(
        title="Potential Account Compromise",
        description="Suspicious authentication activity",
        severity="high",
        alert_ids=[alert.id]
    )

    assert len(incident.alert_ids) == 1
    assert incident.alert_ids[0] == alert.id


def test_reject_unknown_fields():
    with pytest.raises(ValueError):
        Alert(
            title="Suspicious Login",
            description="Test",
            source="Sentinel",
            severity="high",
            unknown_field="unexpected"
        )
