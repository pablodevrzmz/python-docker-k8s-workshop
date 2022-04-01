class Subscription:
    def __init__(self, dic) -> None:
        self.id = str(dic["_id"])
        self.exp_date = dic["exp_date"]
        self.manifest = dic["manifest"]
        self.status = dic["status"]