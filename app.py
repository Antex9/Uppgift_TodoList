from flask import Flask
import flask.ext.restful as rest

app = Flask(__name__)
api = rest.Api(app)

from models import *

app = Flask(__name__)
api = rest.Api(app)

db.bind('sqlite', 'todo_api.db', create_db=True)
db.generate_mapping(create_tables=True)

class Todos(rest.Resource):
    def get(self):
        """Will give you all the todo items"""

        with orm.db_session:
            return {
                item.id: {
                    'task': item.data,
                    'tags': [tag.id for tag in item.tags]
                }
                for item in Todo.select()
            }
'tags': [tag.url for tag in item.tags]

import json

from flask import Flask, request
import flask.ext.restful as rest
    "data": "Buy Milk!",
    "tags": ["work", "high"]

def put(self):
    """Payload contains information to create new todo item"""

    info = json.loads(request.data)

    with orm.db_session:
        item = Todo(data=info['data'])

        for tag_name in info['tags']:
            tag = Tag.get(name=tag_name)
            if tag is None:
                tag = Tag(name=tag_name)
            item.tags += tag

    return {}, 200
