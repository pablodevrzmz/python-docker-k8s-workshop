from abc import ABC, abstractmethod

class ISubscriptionService(ABC):
    @abstractmethod
    def get_subscriptions(self):
        pass