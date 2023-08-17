import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s --<>-- %(name)s --<>-- %(levelname)s --<>-- %(message)s\n-------')
ch.setFormatter(formatter)
logger.addHandler(ch)


class DefaultException(Exception):
    def __init__(self, key):
        message = (
            "Exception in default\n"
            f"Key was: {key}"
        )
        self.custom_val = "Some custom val"
        super().__init__(message)


class ExceptionA(Exception):
    ...


class ExceptionB(Exception):
    ...


class ExceptionC(Exception):
    ...

# ---- Logging
# def default() -> None:
#     a = {}
#     try:
#         a[1]
#     except KeyError:
#         logger.exception("Msg")
#         raise


def default() -> None:
    a = {}
    key = 555
    try:
        a[key]
    except (KeyError, DefaultException) as e:
        raise DefaultException(key)


def a() -> None:
    try:
        default()
    except (KeyError, DefaultException):
        logger.critical("Msg A", exc_info=True)


# Exceptions
def b() -> None:
    try:
        default()
    except (KeyError, DefaultException) as e:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        raise ExceptionB("Msg B") from e


def c() -> None:
    try:
        default()
    except (KeyError, DefaultException) as e:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        raise ExceptionC("Msg C")


if __name__ == "__main__":
    # a()
    # b()
    c()
