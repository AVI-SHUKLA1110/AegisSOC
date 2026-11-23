
import json
from pathlib import Path
from pydantic import ValidationError
from app.connectors.base import SIEMConnector
from app.schemas.alert import Alert


class MockSIEMConnector(SIEMConnector):

    def __init__(self, file_path: str = "sample_data/alerts.json"):
        self.file_path = Path(file_path)

    def fetch_alerts(self) -> list[Alert]:
        with self.file_path.open("r", encoding="utf-8") as file:
            raw_alerts = json.load(file)

        valid_alerts = []
        failed_alerts = []

        for index, raw_alert in enumerate(raw_alerts):
            try:
                alert = Alert.model_validate(raw_alert)
                valid_alerts.append(alert)

            except ValidationError as error:
                failed_alerts.append({
                    "index": index,
                    "error": str(error)
                })

        print(f"Successfully ingested: {len(valid_alerts)}")
        print(f"Failed validation: {len(failed_alerts)}")

        return valid_alerts