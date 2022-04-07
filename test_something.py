from typing import overload


class Error:
    pass


class Superclass:
    def error_log(self) -> Error:
        pass


class Subclass(Superclass):
    @overload
    def error_log(self) -> int:
        pass
