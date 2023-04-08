class NotDefinedError(Exception):
    detail: str = "The requested object is not defined."
    status_code: int = 500