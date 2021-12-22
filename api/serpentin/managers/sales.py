from datetime import date
from dateutil.parser import parse

from serpentin.models.sales import Sales
from serpentin.managers.deals import get_deals_of_month_by_sales
from serpentin.managers.statements import get_statement_of_month_by_sales

def get_sales():
    return Sales.objects()

def compute_progress(sales, date=date.today(), deals=None):
    if deals == None:
        deals = get_deals_of_month_by_sales(date.year, date.month, sales.name)
    total = sum([d.amount for d in deals if d.closed])
    return total / sales.target

def get_sales_by_name(name):
    return Sales.objects(name=name).first()

def get_sales_by_name_with_infos(name, month):
    sales = get_sales_by_name(name)
    if month is None:
        month = date.today()
    else:
        month = parse(month + "-01")
    deals = get_deals_of_month_by_sales(month.year, month.month, sales.name)
    statementCompensations = get_statement_of_month_by_sales(month.year, month.month, sales.name).compensations
    return sales, deals, statementCompensations
