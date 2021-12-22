import datetime

from mongoengine.queryset.visitor import Q
from serpentin.models.deals import Deal
from serpentin.models.sales import Sales

def get_deals():
    return Deal.objects()

def get_deals_by_sales(salesName):
    sales = Sales.objects(name=salesName).first()
    return Deal.objects(owner=sales)

def get_deals_of_month_by_sales(year, month, salesName):
    sales = Sales.objects(name=salesName).first()
    first_day_of_month = datetime.datetime(year, month, 1)
    first_day_of_next_month = datetime.datetime(year + ((month + 1) // 12), (month + 1) % 12, 1)
    return Deal.objects(
        Q(owner=sales) &
        Q(active=True) &
        Q(close_date__gte=first_day_of_month) &
        Q(close_date__lt=first_day_of_next_month))

