
import json
from pathlib import Path

from app.connectors.base import SIEMConnector
from app.schemas.alert import Alert


class MockSIEMConnector(SIEMConnector):

    def __init__(self, file_path: str = "sample_data/alerts.json"):
        self.file_path = Path(file_path)

    def fetch_alerts(self) -> list[Alert]:

        with self.file_path.open("r", encoding="utf-8") as file:
            raw_alerts = json.load(file)

        alerts = [
            Alert.model_validate(alert)
            for alert in raw_alerts
        ]

        return alerts
