from mongoengine import Document, StringField, FloatField


class Sales(Document):
    name = StringField()
    target = FloatField()

    def get_formatted_data(self):
        return {
            "name": self.name,
            "target": self.target,
            "id": str(self.id)
        }


