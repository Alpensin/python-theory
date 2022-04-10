import unittest
from decorators_theme.fake_auth_and_perm_decs import (
    run_action,
    AuthorizationException,
    PermissionException,
)


class MyTestCase(unittest.TestCase):
    def test_ok(self):
        request = {"login": "Petya", "password": "123", "has_permission": True}
        self.assertEqual(run_action(request), "Секретная информация")

    def test_bad_login(self):
        request = {"login": "Pety", "password": "123", "has_permission": True}
        with self.assertRaises(AuthorizationException):
            run_action(request)

    def test_bad_pass(self):
        request = {
            "login": "Petya",
            "password": "1234",
            "has_permission": True,
        }
        with self.assertRaises(AuthorizationException):
            run_action(request)

    def test_no_permission(self):
        request = {
            "login": "Petya",
            "password": "123",
            "has_permission": False,
        }
        with self.assertRaises(PermissionException):
            run_action(request)


if __name__ == "__main__":
    unittest.main()
