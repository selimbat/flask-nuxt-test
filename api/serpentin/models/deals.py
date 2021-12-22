from mongoengine import (
    BooleanField,
    DateTimeField,
    Document,
    FloatField,
    ReferenceField,
    StringField,
)
from serpentin.models.sales import Sales


class Deal(Document):
    name = StringField(required=True)
    active = BooleanField(required=True, default=True)
    modified = BooleanField(required=True, default=False)

    amount = FloatField()
    closed = BooleanField()
    close_date = DateTimeField()
    owner = ReferenceField(Sales)

    def get_formatted_data(self):
        return {
            "name": self.name,
            "active": self.active,
            "modified": self.modified,
            "amount": self.amount,
            "closed": self.closed,
            "close_date": str(self.close_date.date())
            if self.close_date is not None
            else None,
            "owner": self.owner.name if self.owner is not None else None,
        }
