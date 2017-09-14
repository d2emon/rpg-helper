from flask_script import Manager, prompt, prompt_bool, prompt_pass
from app import app, db
from .models import User


manager = Manager(usage="User management")
# from d2lib import printfile
# from mud.talker import talker

USERNAME_PROMPT = "By what name shall I call you?\n*\t"
USERNAME_CONFIRM = "Did I get the name right {}? "
PASSWORD_PROMPT = "This user already exists, what is the password? "
NEW_USER_PASSWORD_PROMPT = "Give me a password for this user "
TRIES = 3


def cls():
    print("\n" * 80)


def crapup(text=""):
    prompt_pass("\n{}\n\nHit Return to Continue...\n".format(text), default="")

    import sys
    sys.exit(0)


def login(username=""):
    '''
    Does all the login stuff
    The whole login system is called from this
    '''
    user = User.login(username)

    # Get the user name
    while not user:
        user = input_username()

    if user.is_new:
        register(user)
        user.qnmrq = True
        user.ttyt = 0
    else:
        # Password checking
        authenticate(user)
    cls()

    return user


def authenticate(user):
    '''
    Main login code
    '''
    tries = TRIES
    while tries:
        try:
            password = prompt_pass(PASSWORD_PROMPT)
            return user.verify_password(password)
        except AssertionError as e:
            print(e)
            tries -= 1
        assert tries > 0, "Wrong password!"
    return True


def register(user):
    '''
    this bit registers the new user
    '''
    print("Creating new user...")

    password = None
    while True:
        try:
            user.password = prompt_pass(NEW_USER_PASSWORD_PROMPT)
            break
        except AssertionError as e:
            print(e)
    db.session.add(user)
    db.session.commit()
    return True


def input_username(username="", prompt_str=USERNAME_PROMPT):
    if not username:
        username = prompt(prompt_str)[:15]

    user = User.query.by_username(username)
    if user:
        return user

    # If he/she doesnt exist
    if prompt_bool(USERNAME_CONFIRM.format(username)):
        return User(username=username.lower())
    return user


@manager.command
def title():
    '''
    Check for all the created at stuff
    We use stats for this which is a UN*X system call
    '''
    cls()
    time_created = 0
    time_elapsed = 0
    print("""
                     A B E R  M U D

              By Alan Cox, Richard Acott Jim Finnis

    This AberMUD was created: {}
    {}
    """.format(time_created, time_elapsed))


@manager.command
def motd():
    '''
    list the message of the day
    '''
    cls()
    app.logger.debug("printfile(FILES['MOTD'])")
    prompt_pass("", default="")
    print("\n\n")


@manager.option('-n', '--name', dest='username', default=None)
def management(username):
    "Manage users"
    # if username is not None:
    #     # # Now check the option entries
    #     # # -n(name)
    #     # # user = User.by_username(username)
    #     # # print("USER is", user)
    #     # # if user:
    #     # #    # authenticate(user)
    #     # # else:
    #     pass
    # else:
    #     app.logger.debug("getty()")
    if not username:
        title()

    user = login(username)
    if not user.qnmrq:
        motd()

    # Log entry
    app.logger.info("Game entry by %s : UID %s", user, user.uid)

    # Run system
    app.logger.debug("talker(user)")

    # Exit
    prompt_pass("\nBye Bye\n\nHit Return to Continue...\n", default="")
