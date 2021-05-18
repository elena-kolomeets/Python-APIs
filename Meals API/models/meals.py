from mongoengine import Document, StringField, FloatField


class Meals(Document):
    """
     Template for a mongoengine document, which represents a user's favorite meal.
    """
    name = StringField(required=True, unique=True)
    description = StringField(default='')
    price = FloatField(default=0)
    image_url = StringField(default='')
