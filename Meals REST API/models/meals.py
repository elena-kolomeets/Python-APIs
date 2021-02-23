from mongoengine import Document, StringField, FloatField


class Meals(Document):
    """
     Template for a mongoengine document, which represents a user's favorite meal.
    """
    name = StringField(required=True)
    description = StringField()
    price = FloatField()
    image_url = StringField()
