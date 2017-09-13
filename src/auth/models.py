from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from app import db, login_manager


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


class User(UserMixin, db.Model):
    """
    Create an User table
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # email = db.Column(db.String(60), index=True, unique=True)
    # first_name = db.Column(db.String(60), index=True)
    # last_name = db.Column(db.String(60), index=True)
    # department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    role = db.relationship('Role', backref='users', lazy='dynamic')

    def __repr__(self):
        return '<User: {}>'.format(self.username)

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
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        if not self.role:
            return False
        else:
            return self.role.is_admin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
