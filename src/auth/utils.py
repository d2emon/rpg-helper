from flask_script import prompt, prompt_pass, prompt_bool
from .models import User
from app import app


USERNAME_PROMPT = "By what name shall I call you?\n*\t"
USERNAME_CONFIRM = "Did I get the name right {}? "
PASSWORD_PROMPT = "This user already exists, what is the password? "
NEW_USER_PASSWORD_PROMPT = "Give me a password for this user "


def cls():
    print("\n" * 80)


def crapup(text=""):
    prompt_pass("\n{}\n\nHit Return to Continue...\n".format(text), default="")

    import sys
    sys.exit(0)


def input_username(username="", prompt_str=USERNAME_PROMPT):
    # Get the user name
    user = None
    while not user:
        if not username:
            username = prompt(prompt_str)[:15]

        user = User.login(username)
        if user:
            return user

        # If he/she doesnt exist
        if prompt_bool(USERNAME_CONFIRM.format(username)):
            return User(username=username.lower())
    return None


def input_password(password="", prompt_str=PASSWORD_PROMPT):
    if not password:
        password = prompt_pass(prompt_str)
    return password


def input_new_password(user=None, password="", prompt_str=NEW_USER_PASSWORD_PROMPT):
    while True:
        password = input_password(password=password, prompt_str=prompt_str)
        try:
            user.password = password
            break
        except AssertionError as e:
            print(e)
            password = None
    return password


def list_users():
    users = User.query.all()
    for u in users:
        print("{}:\t{}".format(u.id, u.username))
    return prompt("\nUser Name: ")


def show_user(username):
    user = User.query.by_username(username)
    if user is None:
        print("\nNo user registered in that name\n\n")
        return None

    print("\n\n")
    print("User Data For\t{}\n".format(user.username))
    print("Name:\t\t{}".format(user.username))
    print("Password:\t{}".format(user.password_hash))
    print("Role:\t\t{}".format(user.role))
    print("Is Admin:\t{}".format(user.is_admin))
    return user


def show_menu(menu_items, description="", **kwargs):
    cls()
    actions = {action['id']: action['action'] for action in menu_items}
    while True:
        print(description)
        print("Options\n")
        for action in menu_items:
            print("{}] {}".format(action['id'], action['text']))
        print("\n\n")
        answer = input("Select > ").lower()
        action = actions.get(answer)
        if action is None:
            cls()
            print("Bad Option({})".format(answer))
        else:
            action(**kwargs)
