from flask import Blueprint
from flask_restful import Api

from myapi.api.resources import UserResource, UserList, TweetResource, TweetList


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(TweetResource, '/tweets/<int:tweet_id>')
api.add_resource(TweetList, '/tweets')