from mongoengine.queryset.visitor import Q
from serpentin.models.statements import Statement, StatementCompensation
from serpentin.models.compensations import Compensation
from serpentin.models.sales import Sales
from serpentin.managers.compensations import get_compensations, apply_compensation_to_deals
from serpentin.managers.deals import get_deals_of_month_by_sales


def get_statements():
    return Statement.objects()

def get_all_statements_by_sales(salesName):
    sales = Sales.objects(name=salesName).first()
    return Statement.objects(sales=sales)

def get_statement_of_month_by_sales(year, month, salesName):
    sales = Sales.objects(name=salesName).first()
    # The statement for the month is created when we request it for the first time
    statement = Statement.objects(Q(year=year) & Q(month=month) & Q(sales=sales)).first()
    if (statement is None):
        deals = get_deals_of_month_by_sales(int(year), int(month), salesName)
        # By default, we apply all the compensations in the db but this could be configured in the Sales model for instance.
        compensations = [StatementCompensation(
            compensation = c,
            amount = apply_compensation_to_deals(sales, c, deals)
        ) for c in get_compensations() if not c.draft]

        statement = Statement(
          sales=sales,
          month=month,
          year=year,
          compensations=compensations
        ).save()
    #else:
        # If we find a statement, we have to recompute it if there are changes in the deals of the month since the last calculation
        # we can add a 'dirty' flag on the statements that we switch to true when adding or changing a deal
    return statement