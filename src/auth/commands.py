from flask_script import Manager, prompt_pass
from app import app, db
from .models import User, Role
from .utils import cls, input_username, input_password, input_new_password, show_title, show_motd, show_menu, list_users, show_user
# from .menu import admin_option


manager = Manager(usage="User management")
# from d2lib import printfile

TRIES = 3


def login(username="", password=""):
    '''
    Does all the login stuff
    The whole login system is called from this
    '''
    user = input_username(username)
    if user.is_new:
        register_user(user, password=password)
    else:
        authenticate(user)
    cls()
    return user


def authenticate(user):
    '''
    Main login code
    Password checking
    '''
    tries = TRIES
    while tries:
        password = input_password()
        try:
            assert user.verify_password(password) is True, "Wrong password"
            return True
        except AssertionError as e:
            print(e)
            tries -= 1
        assert tries > 0, "Wrong password!"
    return True


def register_user(user=None, username=None, password=None, role=None):
    '''
    this bit registers the new user
    '''
    if user is None:
        user = input_username(username)
    assert User.query.by_username(username) is None, "User allready exists"

    print("Creating new user...")
    password = input_new_password(user, password)
    if role:
        user.role = role
    user.register()
    db.session.add(user)
    db.session.commit()
    return True


def assert_admin(user=None):
    if user is None:
        user = login()
    assert user.is_admin is True, "Access Denied"
    return user


def search_user(search=None):
    if search is None:
        search = list_users()
    print(search)
    # user = User.query.by_username(username)
    return show_user(search)


# Menu Items


@manager.option('-n', '--name', dest='username', default=None)
def change_password(username=None, user=None):
    cls()
    if user is None:
        user = User.query.by_username(username)
    try:
        old_password = input_password(prompt_str="\nOld Password\n*\t")
        assert user.verify_password(old_password) is True, "Incorrect password"
    except AssertionError as e:
        print(e)
        return

    while True:
        try:
            password = input_password(prompt_str="\nNew Password\n*\t")
            verify = input_password(prompt_str="\nVerify Password\n*\t")
            assert verify == password, "Passwords doesn't match"
            user.password = password
        except AssertionError as e:
            print(e)
            continue
        break

    db.session.add(user)
    db.session.commit()
    print("Changed")
    return


@manager.option('-n', '--name', dest='username', default=None)
# @admin_option
def show(username=None, **kwargs):
    """
    Show user data
    """
    user = assert_admin(kwargs.get('user'))
    cls()
    print(user, username)
    s = search_user(username)
    prompt_pass("\nHit Return...", default="")


@manager.option('-n', '--name', dest='username', default=None)
# @admin_option
def edit(username=None, **kwargs):
    """
    Edit user data
    """
    user = assert_admin(kwargs.get('user'))
    cls()
    print(user, username)
    s = search_user(username)
    if s is None:
        s = User(username=username)
    print("\nEditing : {}\n".format(username))
    # try:
    #     shuser.username = edit_field("Name: ", shuser.username)
    #     shuser.password = edit_field("Password: ", shuser.password)
    #     shuser.save(session)
    #     print("{} saved".format(shuser.username))
    # except AssertionError as e:
    #     print(e)
    #     print("Changes not saved")


@manager.option('-n', '--name', dest='username', default=None)
# @admin_option
def del_user(username=None, **kwargs):
    """
    Delete user
    """
    user = assert_admin(kwargs.get('user'))
    cls()
    print(user, username)
    s = search_user(username)
    assert s is not None, "\nCannot delete non-existant user"
    db.session.delete(s)
    db.session.commit()


def exit_mud(username=None, user=None):
    print("Bye!")
    import sys
    sys.exit(0)


@manager.command
def title():
    '''
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    '''
    show_title()


@manager.command
def motd(show=True):
    '''
    list the message of the day
    '''
    if not show:
        return
    show_motd()


@manager.option('-n', '--name', dest='username', default=None)
@manager.option('-p', '--pass', dest='password', default=None)
def createuser(username, password):
    """
    Creates user
    """
    register_user(username=username, password=password)


@manager.option('-n', '--name', dest='username', default=None)
@manager.option('-p', '--pass', dest='password', default=None)
def createsuperuser(username, password):
    """
    Creates superuser
    """
    admin = Role.query.filter_by(is_admin=True).one()
    register_user(username=username, password=password, role=admin)


menu_items = [
    {'id': '1', 'text': "Change Password\n\n", 'action': change_password},
    {'id': '0', 'text': "Exit\n", 'action': exit_mud},
]

admin_menu_items = menu_items + [
    {'id': 'a', 'text': "Show persona", 'action': show},
    {'id': 'b', 'text': "Edit persona", 'action': edit},
    {'id': 'c', 'text': "Delete persona", 'action': del_user},
]


@manager.option('-n', '--name', dest='username', default=None)
def management(username):
    "Manage users"
    # if username is not None:
    #     # # Now check the option entries
    #     # # -n(name)
    #     # # user = User.by_username(username)
    #     # # if user:
    #     # #    # authenticate(user)
    #     # # else:
    #     pass
    # else:
    #     app.logger.debug("getty()")
    if not username:
        title()

    user = login(username)
    motd(not user.qnmrq)

    # Log entry
    app.logger.info("Game entry by %s : UID %s", user, user.uid)

    # Run system
    if user.qnmrq:
        app.logger.debug("main(\"   --}----- ABERMUD -----{--    Playing as \", user)")
    cls()
    description = "Welcome To AberMUD II [Unix]"
    if user.is_admin:
        mi = admin_menu_items
    else:
        mi = menu_items
    show_menu(mi, description, user=user)

    # Exit
    prompt_pass("\nBye Bye\n\nHit Return to Continue...\n", default="")
