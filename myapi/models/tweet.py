from myapi.extensions import db, pwd_context
from datetime import datetime
# from models import User

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(250), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_v2.id'))

    def __repr__(self):
        return '<Tweet {}>'.format(self.tweet)