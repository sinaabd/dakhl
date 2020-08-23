from json import JSONEncoder
from typing import Any

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expense, Income
import datetime


@csrf_exempt
def submit_expense(request):
    """ submit an expense"""

    print("I'm in submit expense")
    print(request.POST)

    # TODO; validate data, user,token,amount might be fake

    this_token = request.POST["token"]
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()

    Expense.objects.create(user=this_user, text=request.POST['text'], date=date, amount=request.POST['amount'])

    return JsonResponse({
        'status': 'ok',

    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """ submit an Income"""

    print("I'm in submit income")
    print(request.POST)

    # TODO; validate data, user,token,amount might be fake

    this_token = request.POST["token"]
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date'not in request.POST:
        date = datetime.datetime.now()

    Income.objects.create(user=this_user, text=request.POST['text'], date=date, amount=request.POST['amount'])

    return JsonResponse({
        'status': 'ok',

    }, encoder=JSONEncoder)
