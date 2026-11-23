
from app.connectors.mock_siem import MockSIEMConnector
from app.schemas.alert import Alert


def test_mock_siem_fetches_alerts():

    connector = MockSIEMConnector()

    alerts = connector.fetch_alerts()

    assert len(alerts) == 3
    assert alerts[0].external_id == "MOCK-001"
    assert alerts[0].severity.value == "high"


def test_mock_siem_returns_alert_objects():

    connector = MockSIEMConnector()

    alerts = connector.fetch_alerts()

    for alert in alerts:
        assert isinstance(alert, Alert)
        assert alert.id is not None
        assert alert.title
        assert alert.source == "MockSIEM"
