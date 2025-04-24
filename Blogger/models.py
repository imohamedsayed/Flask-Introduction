from datetime import datetime
from Blogger import db, loginManager, app
from flask_login import UserMixin


@loginManager.user_loader
def load_user(userId):
    return User.query.get(int(userId))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default="user.jpg")
    password = db.Column(db.String(60), nullable=False)
    blogs = db.relationship("Blog", backref="author", lazy=True)

    def __repr__(self):
        return f"User ( {self.name}, {self.email}, {self.image} )"


class Blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=False, default="blog.png")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Blog ( {self.title}, {self.created_at} )"


with app.app_context():
    db.create_all()
