from accounting.models import Transaction
from ajax_testing.decorators import save_request


@save_request
def add_transaction(date, amount, is_income=False):
    Transaction.objects.create(date=date, amount=amount, is_income=is_income)
    return True