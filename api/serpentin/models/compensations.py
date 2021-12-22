from mongoengine import Document, StringField, BooleanField


class Compensation(Document):
    name = StringField(required=True)
    type = StringField(required=True, choices=["Simple", "Complex"])
    draft = BooleanField(required=True, default=False)


    def get_formatted_data(self):
        return {
            "name": self.name,
            "type": self.type,
            "draft": self.draft
        }
