from pages import login_page
from pages import home_page
from helpers.navigator import get
from dto.user import name, password
from assertions.c_assert import assert_on_home_page
from assertions.c_assert import assert_on_login


def test_login():
    get(login_page)
    assert_on_login()
    login_page.login((name, password))
    get(home_page)
    assert_on_home_page()
    home_page.logout()
    assert_on_login()


if __name__ == '__main__':
    test_login()
