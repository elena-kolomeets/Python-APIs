from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, ListField, StringField, EmailField, \
    BooleanField, ReferenceField
from flask_bcrypt import generate_password_hash, check_password_hash

from models.meals import Meals


class Access(EmbeddedDocument):
    """
    Custom EmbeddedDocument to set user authorizations.
    """
    user = BooleanField(default=True)
    admin = BooleanField(default=False)


class Users(Document):
    """
    Template for a mongoengine Document, which represents a user.
    Password is automatically hashed before saving.
    """
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    access = EmbeddedDocumentField(Access, default=Access(user=True, admin=False))
    fav_meals = ListField(ReferenceField(Meals))
    name = StringField()

    def generate_pwd_hash(self):
        # hash the password with BCrypt method
        # if len(self.password) < 20:     # prevent double hashing
        self.password = generate_password_hash(password=self.password).decode('utf-8')

    def check_pwd_hash(self, password: str) -> bool:
        # check the hash against the password with BCrypt method
        return check_password_hash(pw_hash=self.password, password=password)

    def save(self, *args, **kwargs):
        # Overwrite Document.save() method to enable password hashing before saving
        # Should only work once otherwise generates
        # new hashes which do not match anymore
        if self._created:
            self.generate_pwd_hash()
        super(Users, self).save(*args, **kwargs)
