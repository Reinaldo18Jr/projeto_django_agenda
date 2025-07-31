from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from contact.models import Contact

def create(request):
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context
    )
