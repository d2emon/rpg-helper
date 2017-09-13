from flask_script import Manager, prompt_bool
from app import app


manager = Manager(usage="User management")
# from d2log import mud_logger as logger, load_logger
# from d2lib import printfile
# from mud.utils import getty, cls, crapup
# from mud.talker import talker
# from user.models import User
# from user.login import chknolog, login  # , authenticate


@manager.option('-n', '--name', dest='username', default=None)
def management(username):
    "Manage users"
    app.logger.debug("check_host(FILES['HOST_MACHINE'])")
    print("\n" * 4)
    # Check if there is a no logins file active
    app.logger.debug("chknolog()")

    user = None

    if username is not None:
        # # Now check the option entries
        # # -n(name)
        # # user = User.by_username(username)
        # # print("USER is", user)
        # # if user:
        # #    # authenticate(user)
        # # else:
        app.logger.debug("user = login(username)")
        app.logger.debug("user.qnmrq = True")
        app.logger.debug("user.ttyt = 0")
    else:
        app.logger.debug("getty()")

    if user is None:
        app.logger.debug("show_title()")
        app.logger.debug("user = login()")

    # if not user.qnmrq:
    #     show_motd()

    # Log entry
    # try:
    #     uid = os.getuid()
    # except:
    #     uid = '<UID>'
    app.logger.info("Game entry by %s : UID %s", "user.username", "uid")

    # Run system
    app.logger.debug("talker(user)")
    print("db.create_all()")
    if prompt_bool("Are you sure? You will lose all your data!"):
        print("db.drop_all()")


    # Exit
    app.logger.debug("crapup(\"Bye Bye\")")
