import requests
import os
from django.shortcuts import render, redirect
from dotenv import load_dotenv

from django.shortcuts import render, get_object_or_404
from .models import Case


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def works(request):
    return render(request, 'our-works.html')

def techimpuls(request):
    return render(request, 'techimpuls.html')

def triphouse(request):
    return render(request, 'triphouse.html')

def moloko(request):
    return render(request, "moloko.html")

def bookingrent(request):
    return render(request, "bookingrent.html")

def sdelkipro(request):
    return render(request, "sdelkipro.html")

def works(request):
    cases = Case.objects.filter(is_published=True).prefetch_related("images").order_by("created_at")
    return render(request, "our-works.html", {"cases": cases})

def case_detail(request, slug):
    case = get_object_or_404(Case.objects.prefetch_related("images"), slug=slug, is_published=True)
    return render(request, "case-detail.html", {"case": case})

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def contact_form(request):
    if request.method == "POST":

        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        company = request.POST.get("company")
        description = request.POST.get("desk_project")

        message = f"""
Новая заявка с сайта PlumIT:

Имя: {name}
Фамилия: {surname}
Телефон: {phone}
Email: {email}
Компания: {company}

Описание:
{description}
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": message
        })

        return redirect('home')