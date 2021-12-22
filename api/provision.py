import calendar
import datetime
import random

from faker import Faker
from serpentin.core.database import connect_to_database
from serpentin.models.deals import Deal
from serpentin.models.sales import Sales
from serpentin.models.compensations import Compensation
from serpentin.models.statements import Statement

connect_to_database()

Deal.drop_collection()
Sales.drop_collection()
Compensation.drop_collection()
Statement.drop_collection()

fake = Faker("fr-FR")

Compensation(
  name="Argent facile",
  type="Simple",
  draft=False
).save()

Compensation(
  name="Bon filon",
  type="Complex",
  draft=False
).save()

Compensation(
  name="Work in progress",
  type="Complex",
  draft=True
).save()

for _ in range(5):
    Sales(
        name=fake.name(),
        target=random.randint(8, 25) * 1000
    ).save()

sales = Sales.objects()

for year in range(2020, 2023):
    for month in range(1, 13):
        month_range = calendar.monthrange(year, month)

        for sale in sales:
            for _ in range(random.randint(2, 10)):
                closed = random.random() > 0.5

                close_date = None
                if closed:
                    close_date = fake.date_between(
                        start_date=datetime.date(month=month, year=year, day=1),
                        end_date=datetime.date(
                            month=month, year=year, day=month_range[1]
                        ),
                    )

                Deal(
                    name=fake.company(),
                    active=True,
                    modified=False,
                    amount=random.randint(10, 50) * 100,
                    closed=closed,
                    close_date=close_date,
                    owner=sale,
                ).save()
