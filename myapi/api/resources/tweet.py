from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from datetime import datetime

from myapi.models import Tweet
from myapi.extensions import ma, db
from myapi.commons.pagination import paginate

class TweetSchema(ma.ModelSchema):
    class Meta:
        model = Tweet
        sqla_session = db.session
        include_fk = True

class TweetResource(Resource):
    method_decorators = [jwt_required]

    def get(self, tweet_id):
        schema = TweetSchema()
        twit = Tweet.query.get_or_404(tweet_id)
        if not twit:
            return {"error": "tweet not found"}, 404
        return {"twit": schema.dump(twit).data}

    # def post(self):
    #     schema = TweetSchema()
    #     tweet, errors = schema.load(request.json)
    #     if errors:
    #         return errors, 422

    #     db.session.add(tweet)
    #     db.session.commit()

    #     return {"msg": "tweet created", "tweet": schema.dump(user).data}, 201
        
    def put(self, tweet_id):
        schema = TweetSchema(partial=True)
        twit = Tweet.query.get_or_404(id=tweet_id)
        twit, errors = schema.load(request.json, instance=twit)

    def delete(self, tweet_id):
        twit = Tweet.query.get_or_404(id=tweet_id)
        db.session.delete(twit)
        db.session.commit()
        return {"msg": "tweet was deleted"}

class TweetList(Resource):
    method_decorators = [jwt_required]

    def get(self):
        schema = TweetSchema()
        query = Tweet.query
        return paginate(query, schema)

    def post(self):
        schema = TweetSchema()
        # tweets = request.json['tweet_user']
        twit, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(twit)
        db.session.commit()

        return {"msg": "tweet was created", "tweet": schema.dump(twit).data}, 201
