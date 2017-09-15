from flask import url_for
from flask_login import UserMixin
from flask_sqlalchemy import BaseQuery
from werkzeug.security import generate_password_hash, check_password_hash
#
from sqlalchemy.orm import validates


from app import app, db, login_manager


class Role(db.Model):
    """
    Create a Role table
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)

    # users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class UserQuery(BaseQuery):
    def by_username(self, username):
        '''
        Return block data for user or -1 if not exist
        '''
        if username is None:
            return None

        # return self.filter(Post.post_name.ilike(name)).distinct().first()
        return self.filter_by(username=username.lower()).first()


class User(UserMixin, db.Model):
    """
    Create an User table
    """
    query_class = UserQuery

    id = db.Column(db.Integer, primary_key=True)
    # username = Column(String(16), nullable=False)
    # password = Column(String(16), nullable=False)
    username = db.Column(
        db.String(60),
        index=True,
        unique=True,
        nullable=False,
        default="",
        info={'label': "Username"}
    )
    password_hash = db.Column(db.String(128))
    # email = db.Column(db.String(60), index=True, unique=True)
    # first_name = db.Column(db.String(60), index=True)
    # last_name = db.Column(db.String(60), index=True)
    # department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    # role = db.relationship('Role', backref='users', lazy='dynamic')
    role = db.relationship('Role', backref='users')
    # person = relationship("Person", uselist=False, back_populates="user")

    nologin = False
    __namegiv = False
    __qnmrq = False
    __ttyt = 0
    __isawiz = False

    def __repr__(self):
        return '<User: {}>'.format(self.fullname)

    # Password management
    @property
    def password(self):
        """
        Prevent password for being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        # assert password == self.password, "Wrong password"
        return check_password_hash(self.password_hash, password)

    # Properties
    @property
    def is_admin(self):
        """
        Return if user is admin
        """
        if not self.role:
            return False
        else:
            return self.role.is_admin

    @property
    def is_new(self):
        """
        Return if user is new
        """
        return not self.id

    @property
    def uid(self):
        # try:
        #     uid = os.getuid()
        # except:
        #     uid = '<UID>'
        return self.id

    @property
    def qnmrq(self):
        return self.__qnmrq

    @qnmrq.setter
    def qnmrq(self, value):
        self.__qnmrq = value

    @property
    def ttyt(self):
        return self.__ttyt

    @ttyt.setter
    def ttyt(self, value):
        self.__ttyt = value

    @property
    def host(self):
        # return socket.gethostname()
        return "Host"

    @property
    def fullname(self):
        username = self.username.capitalize()
        if self.is_admin:
            return "The {}".format(username)
        return username

    @property
    def banned(self):
        '''
        Check to see if UID in banned list
        '''
        if not self.username:
            return False
        c = self.username.lower()

        a = ""  # openlock(BAN_FILE,"r+");
        if a is None:
            return False
        b = ''
        for b in a:
            if b == '\n':
                b = ''
            b = b.lower()
            if b == self.host:
                raise Exception("I'm sorry- that userid has been banned from the Game")
        # fclose(a);
        return False

    @property
    def after_login(self):
        # if employee.is_admin:
        #     return url_for('home.admin_dashboard')
        # else:
        #     return url_for('home.dashboard')
        return url_for('home.dashboard')

    # Other methods
    @classmethod
    def login(cls, username, password=None):
        if not username:
            return None

        user = cls.query.by_username(username.lower())
        if not user:
            return None

        # check_host(FILES['HOST_MACHINE'])
        user.validate_host("host", "Host")

        # Check if there is a no logins file active
        user.validate_nologin()

        # Check if banned first
        if user.banned:
            # cuserid(NULL));
            return None

        return user

    def register(self):
        self.qnmrq = True
        self.ttyt = 0

    @staticmethod
    def chkname(username):
        # assert '.' not in username, "Illegal characters in username"
        # assert ' ' not in username, "Illegal characters in username"
        import re
        return re.match("^\w*$", username)

    # from mud.utils import validname

    # Validators
    @validates('username')
    def validate_username(self, key, username):
        app.logger.debug("USERNAME %s", username)
        assert username is not None
        username = username.strip()
        assert username, "Empty username"
        assert User.chkname(username), "Illegal characters in username"
        # assert validname(username), "Bye Bye"
        return username

    @validates('password')
    def validate_password(self, key, password):
        assert password is not None
        assert password, "Empty password"
        assert '.' not in password, "Illegal characters in password"
        assert ' ' not in password, "Illegal characters in password"
        return password

    def validate_host(self, key, newhost):
        '''
        Check we are running on the correct host
        see the notes about the use of flock();
        and the affects of lockf();
        '''
        assert self.host == newhost, "AberMUD is only available on {}, not on {}".format(newhost, self.host)

    def validate_nologin(self):
        # try:
        #     with open(CONFIG["NOLOGIN"]) as a:
        #         s = a.read()
        #     print(s)
        # except:
        #     return
        assert self.nologin is False, "Nologin"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
