from datetime import datetime, timedelta

from accounting.models import Transaction
from ajax_testing.decorators import save_request


@save_request
def add_transaction(date, amount, is_income=False):
    date = datetime.strptime(date, "%Y/%m/%d")
    Transaction.objects.create(date=date, amount=amount, is_income=is_income)
    return True


@save_request
def get_transactions_by_date(start, end):
    start = datetime.strptime(start, "%Y/%m/%d") if start else datetime.today()+timedelta(days=-1)
    end = datetime.strptime(end, "%Y/%m/%d") if end else datetime.today()
    return Transaction.objects.filter(date__gte=start, date__lte=end).all()


@save_request
def get_sum(transactions):
    paid=0
    get=0
    for t in transactions:
        if t.is_income:
            get = get + t.amount
        else:
            paid = paid + t.amount
    return get, paid


@save_request
def remove_transaction_by_id(id):
    try:
        Transaction.objects.get(id=id).delete()
        return True
    except Exception:
        return False