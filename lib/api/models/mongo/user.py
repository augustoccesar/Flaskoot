from datetime import datetime

from mongoengine import DateTimeField, Document, StringField


class User(Document):
    username = StringField(unique=True, null=False)

    created_at = DateTimeField(default=datetime.utcnow(), null=False)
    updated_at = DateTimeField(default=datetime.utcnow(), null=False)
    deleted_at = DateTimeField(null=True)

    meta = {
        'indexes': [
            '$username'
        ]
    }
