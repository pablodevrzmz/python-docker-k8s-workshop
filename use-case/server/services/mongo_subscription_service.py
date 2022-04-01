
from services.interface_subscription_service import ISubscriptionService
from db.mongo_provider import db as mongodb

class SubscriptionService(ISubscriptionService):

    COLLECTION = "subscriptions"
    __db = mongodb[COLLECTION]

    def get_subscriptions(self):
        data = self.__db.find({})
        return data