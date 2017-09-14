from flask_script import Manager, prompt_pass
from app import app, db
from .models import User, Role
from .utils import cls, input_username, input_password, input_new_password, show_title, show_motd, show_menu
from .menu import menu_items, admin_menu_items


manager = Manager(usage="User management")
# from d2lib import printfile
# from mud.talker import talker

TRIES = 3


def login(username="", password=""):
    '''
    Does all the login stuff
    The whole login system is called from this
    '''
    user = input_username(username)
    if user.is_new:
        register(user, password=password)
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


def register(user=None, username=None, password=None, role=None):
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
def createsuperuser(username, password):
    """
    Creates superuser
    """
    admin = Role.query.filter_by(is_admin=True).one()
    register(username=username, password=password, role=admin)


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
