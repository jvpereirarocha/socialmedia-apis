class Instagram:
    def __init__(self, username, code=None, user_id=None):
        self.username = username
        self.code = code
        self.user_id = user_id

    @classmethod
    def format_data_to_entity(cls, data):
        return cls(
            username=data.get("username"),
            code=data.get("code") or "Not found",
            user_id=data.get("user_id", "Not found"),
        )