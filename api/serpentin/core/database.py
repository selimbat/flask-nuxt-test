from mongoengine import connect


def connect_to_database():
    connect(
        db="serpentin",
        host="mongodb://serpentin:serpentin@localhost:27017/?retryWrites=false&authSource=admin",
        alias="default",
    )
