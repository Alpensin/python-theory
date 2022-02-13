class AuthorizationException(Exception):
    pass


class PermissionException(Exception):
    pass


def login_required(func):
    def wrapper(request):
        if request["login"] != "Petya" or request["password"] != "123":
            raise AuthorizationException
        return func(request)

    return wrapper


def permission_required(func):
    def wrapper(request):
        if not request["has_permission"]:
            raise PermissionException
        return func(request)

    return wrapper


@permission_required
@login_required
def run_action(request):
    return "Секретная информация"


if __name__ == "__main__":
    request = {"login": "Petya", "password": "123", "has_permission": True}
    print(run_action(request))
