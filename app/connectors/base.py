from abc import ABC, abstractmethod
# ABC stands for Abstract Base Class. It lets us define a common interface that other classes must follow.

from app.schemas.alert import Alert


class SIEMConnector(ABC):

    @abstractmethod
    def fetch_alerts(self) -> list[Alert]:
        pass
