# games/models.py

from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom, DateTimeProperty

class User(StructuredNode):
    username = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    friends = RelationshipTo('User', 'FRIEND')
    game_lists = RelationshipTo('GameList', 'HAS_LIST')

class Game(StructuredNode):
    title = StringProperty(unique_index=True, required=True)
    genre = StringProperty()
    release_date = DateTimeProperty()

class GameList(StructuredNode):
    name = StringProperty(required=True)
    owner = RelationshipFrom(User, 'HAS_LIST')
    games = RelationshipTo(Game, 'CONTAINS')

class Review(StructuredNode):
    content = StringProperty(required=True)
    rating = IntegerProperty(min_value=1, max_value=10)
    reviewer = RelationshipFrom(User, 'WROTE_REVIEW')
    game = RelationshipTo(Game, 'REVIEWED')
