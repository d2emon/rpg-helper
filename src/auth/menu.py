from .utils import cls


def admin_option(f):
    def decorated(user, *args, **kwargs):
        if not user.is_admin:
            cls()
            print("This action is not allowed for you.")
            return
        f(user, *args, **kwargs)
        pass
    return decorated


def enter_game(user=None):
    cls()
    print("""
The Hallway
You stand in a long dark hallway, which echoes to the tread of your
booted feet. You stride on down the hall, choose your masque and enter the
worlds beyond the known......

    """)
    # main("   --{----- ABERMUD -----}--    Playing as ", user)


def change_password(user=None):
    cls()
    print("Change password")


def exit_mud(user=None):
    print("Bye!")
    import sys
    sys.exit(0)


@admin_option
def test_game(user=None):
    cls()
    print("Test game")


@admin_option
def show_user(user=None):
    cls()
    print("Show user")


@admin_option
def edit_user(user=None):
    cls()
    print("Edit user")


@admin_option
def del_user(user=None):
    cls()
    print("Del user")


menu_items = [
    {'id': '1', 'text': "Enter The Game", 'action': enter_game},
    {'id': '2', 'text': "Change Password\n\n", 'action': change_password},
    {'id': '0', 'text': "Exit\n", 'action': exit_mud},
]

admin_menu_items = menu_items + [
    {'id': '4', 'text': "Run TEST game", 'action': test_game},
    {'id': 'a', 'text': "Show persona", 'action': show_user},
    {'id': 'b', 'text': "Edit persona", 'action': edit_user},
    {'id': 'c', 'text': "Delete persona", 'action': del_user},
]
