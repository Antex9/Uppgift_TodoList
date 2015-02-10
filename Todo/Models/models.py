from pony import orm  # 1

db = orm.Database()  # 2


class Todo(db.Entity):  # 3

    _table_ = 'Todos' # 4

    data = orm.Required(unicode)  # 5
    tags = orm.Set("Tag")  # 6


class Tag(db.Entity):

    _table_ = 'Tags'

    name = orm.Required(unicode, unique=True)  # 7
    tags = orm.Set("Todo") # 8

@property
def url(self):
    return "http://localhost:5000/tags/{}".format(self.id)