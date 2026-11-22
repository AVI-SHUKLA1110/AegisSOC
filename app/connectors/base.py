from abc import ABC, abstractmethod

from app.schemas.alert import Alert


class SIEMConnector(ABC):

    @abstractmethod
    def fetch_alerts(self) -> list[Alert]:
        pass
