from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
import requests
import json

from .forms import PayForm


def payment_form_view(request):
    form = PayForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, 'payment/index.html', context)
