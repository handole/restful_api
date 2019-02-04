from myapi.extensions import db, pwd_context

# from .tweet import Tweet


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user_v2.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user_v2.id'))
)

class User(db.Model):
    """Basic user model
    """
    __tablename__ = "user_v2"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tweets = db.relationship('Tweet', backref='tweet_user', lazy='dynamic')
    followed = db.relationship('User', secondary=followers,
                    primaryjoin=(followers.c.follower_id == id),
                    secondaryjoin=(followers.c.followed_id == id),
                    backref=db.backref('follower', lazy='dynamic'), lazy='dynamic')

    active = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return "<User %s>" % self.username

    def follow(self, user):
        if not self. is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id
        ).count() > 0

    def followed_tweet(self):
        followed = Tweet.query.join(
            followers, (followers.c.followed_id == Tweet.user_id)).filter(
                followers.c.followed_id == self.id)
        own = Tw    .query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Tweet.timestamp.desc())

