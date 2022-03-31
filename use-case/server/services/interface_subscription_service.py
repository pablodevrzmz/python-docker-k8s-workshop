from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def get_subscription(self):
        pass