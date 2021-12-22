from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    FloatField,
    IntField,
    ReferenceField,
)
from serpentin.models.compensations import Compensation
from serpentin.models.sales import Sales


class StatementCompensation(EmbeddedDocument):
    compensation = ReferenceField(Compensation)
    amount = FloatField(required=True)

    def get_formatted_data(self):
        return {
            "compensation": self.compensation.get_formatted_data(),
            "amount": self.amount,
        }


class Statement(Document):
    sales = ReferenceField(Sales, required=True)
    month = IntField(required=True)
    year = IntField(required=True)

    compensations = EmbeddedDocumentListField(StatementCompensation, default=[])

    def get_formatted_data(self):
        return {
            "sales": self.sales.name,
            "month": self.month,
            "year": self.year,
            "compensations": [c.get_formatted_data() for c in self.compensations],
        }
