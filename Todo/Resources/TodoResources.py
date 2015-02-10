class Todos(rest.Resource):

    def get(self):
        """Will give you all the todo items"""
        return {}

    def put(self):
        """Payload contains information to create new todo item"""
        return {}


class TodoItem(rest.Resource):

    def get(self, todo_id):
        """
        Get specific information on a Todo item

        :param todo_id: The Todo Item's ID, which is unique and a primary key
        :type todo_id: int
        """
        return {}


class Tags(rest.Resource):

    def get(self):
        """Will show you all tags"""
        return {}


class TagItem(rest.Resource):

    def get(self, tag_id):
        """
        Will show you information about a specific tag

        :param tag_id: ID for the tag
        :type tag_id: int
        """
        return {}













