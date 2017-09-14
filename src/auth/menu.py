from .utils import cls, input_username, input_password, input_new_password, show_title, show_motd


def enter_game(user):
    cls()
    print("Enter game")


def change_password(user):
    cls()
    print("Change password")


def exit_mud(user):
    print("Bye!")
    import sys
    sys.exit(0)


def test_game(user):
    cls()
    print("Test game")


def show_user(user):
    cls()
    print("Show user")


def edit_user(user):
    cls()
    print("Edit user")


def del_user(user):
    cls()
    print("Del user")


menu_items = {
    '1': enter_game,
    '2': change_password,
    '0': exit_mud,
    '4': test_game,
    'a': show_user,
    'b': edit_user,
    'c': del_user,
}
