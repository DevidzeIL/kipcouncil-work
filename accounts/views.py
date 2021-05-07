from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta, date
import calendar

from django.utils.html import mark_safe

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import (
    Company, Student, UserFunction, UserAward, 
    UserComment, Tag, Event, Member, New,
    DocsCollege, DocsCouncil, About
)
from .forms import CreateUserForm, StudentForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from .utils import Calendar



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, username + ' был зарегистрирован!')

            return redirect('login')

    context = {
        'form':form
    }
    return render(request, 'accounts/auth/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Логин или пароль указан неверно')

    context = {}
    return render(request, 'accounts/auth/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def userPage(request):
    events = request.user.student.member_set.all()

    events_CULTURE_c = Event.objects.filter(tags__name="Культмасс").count()
    events_SPORT_c = Event.objects.filter(tags__name="Спорт").count()


    context = {
        'events':events, 
        'events_CULTURE_c':events_CULTURE_c, 'events_SPORT_c':events_SPORT_c
    }
    return render(request, 'accounts/auth/user.html', context)



@login_required(login_url='login')
def accountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

        
    context = {'form':form}
    return render(request, 'accounts/auth/account_settings.html', context)


def main(request):

    post_ALL = New.objects.filter(tags__name="Общее").last()
    post_CULTURE = New.objects.filter(tags__name="Культмасс").last()
    post_SPORT = New.objects.filter(tags__name="Спорт").last()
    post_PROF = New.objects.filter(tags__name="Профка").last()
    post_INFORM = New.objects.filter(tags__name="Информ").last()
    post_MEDIA = New.objects.filter(tags__name="Мультимедиа").last()
    post_CLUBS = New.objects.filter(tags__name="Кружки").last()

    context = {
        'post_ALL':post_ALL, 'post_CULTURE':post_CULTURE,
        'post_SPORT':post_SPORT, 'post_PROF':post_PROF,
        'post_INFORM':post_INFORM, 'post_MEDIA':post_MEDIA,
        'post_CLUBS':post_CLUBS
    }

    return render(request, 'accounts/pages/home.html', context)



def direction(request, tags):
    news = New.objects.filter(tags=tags)
    users = UserFunction.objects.filter(tags=tags)
    text_about = About.objects.filter(tags=tags).last()

    context = {
    'news':news, 'users':users, 'text_about':text_about
    }
    return render(request, 'accounts/pages/direction.html', context)



def about(request):
    users = UserFunction.objects.filter(tags__name="Общее")
    text_about = About.objects.filter(tags__name="Общее").last()

    context = {
        'users':users, 'text_about':text_about
    }
    return render(request, 'accounts/pages/about.html', context)



def docs_college(request):
    docs_college_PCS_1 = DocsCollege.objects.filter(specialty="ПКС", cource="1 курс")
    docs_college_PCS_2 = DocsCollege.objects.filter(specialty="ПКС", cource="2 курс")
    docs_college_PCS_3 = DocsCollege.objects.filter(specialty="ПКС", cource="3 курс")
    docs_college_PCS_4 = DocsCollege.objects.filter(specialty="ПКС", cource="4 курс")

    docs_college_OIBS_1 = DocsCollege.objects.filter(specialty="ОИБАС", cource="1 курс")
    docs_college_OIBS_2 = DocsCollege.objects.filter(specialty="ОИБАС", cource="2 курс")
    docs_college_OIBS_3 = DocsCollege.objects.filter(specialty="ОИБАС", cource="3 курс")
    docs_college_OIBS_4 = DocsCollege.objects.filter(specialty="ОИБАС", cource="4 курс")

    docs_college_ISIP_1 = DocsCollege.objects.filter(specialty="ИСИП", cource="1 курс")
    docs_college_ISIP_2 = DocsCollege.objects.filter(specialty="ИСИП", cource="2 курс")
    docs_college_ISIP_3 = DocsCollege.objects.filter(specialty="ИСИП", cource="3 курс")
    docs_college_ISIP_4 = DocsCollege.objects.filter(specialty="ИСИП", cource="4 курс")

    context = {
    'docs_college_PCS_1':docs_college_PCS_1, 'docs_college_PCS_2':docs_college_PCS_2,
    'docs_college_PCS_3':docs_college_PCS_3, 'docs_college_PCS_4':docs_college_PCS_4,
    'docs_college_OIBS_1':docs_college_OIBS_1, 'docs_college_OIBS_2':docs_college_OIBS_2,
    'docs_college_OIBS_3':docs_college_OIBS_3, 'docs_college_OIBS_4':docs_college_OIBS_4,
    'docs_college_ISIP_1':docs_college_ISIP_1, 'docs_college_ISIP_2':docs_college_ISIP_2,
    'docs_college_ISIP_3':docs_college_ISIP_3, 'docs_college_ISIP_4':docs_college_ISIP_4}
    return render(request, 'accounts/pages/docs_college.html', context)



def docs_council(request):
    docs_council_ALL = DocsCouncil.objects.filter(direction="ОБЩЕЕ")
    docs_council_CULTURE = DocsCouncil.objects.filter(direction="КУЛЬТМАСС")
    docs_council_SPORT = DocsCouncil.objects.filter(direction="СПОРТ")
    docs_council_PROF = DocsCouncil.objects.filter(direction="ПРОФКА")
    docs_council_INROFM = DocsCouncil.objects.filter(direction="ИНФОРМ")
    docs_council_MEDIA = DocsCouncil.objects.filter(direction="МУЛЬТИМЕДИА")
    docs_council_CLUBS = DocsCouncil.objects.filter(direction="КРУЖКИ")

    context = {
    'docs_council_ALL':docs_council_ALL, 'docs_council_CULTURE':docs_council_CULTURE,
    'docs_council_SPORT':docs_council_SPORT, 'docs_council_PROF':docs_council_PROF,
    'docs_council_INROFM':docs_council_INROFM, 'docs_council_MEDIA':docs_council_MEDIA,
    'docs_council_CLUBS':docs_council_CLUBS
    }
    return render(request, 'accounts/pages/docs_council.html', context)



def news_about(request, pk_test):
    new = New.objects.get(id=pk_test)
    event = new.event
    members = Member.objects.filter(event = new.event)

    
    context = {
        'members':members, 'new':new, 'event':event
    }
    print('context:::', context)
    return render(request, 'accounts/pages/news_about.html', context)



def news(request):
    news_list = New.objects.all()
    context = {
        'news_list':news_list
    }
    return render(request, 'accounts/pages/news.html', context)



def search(request):
    return render(request, 'accounts/pages/search.html')




def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def calendar_view(request):
    mydate = get_date(request.GET.get('month', None))
    cal = Calendar(mydate.year, mydate.month)
    html_cal = mark_safe(cal.formatmonth(withyear=True))
    events = Event.objects.all()

    p_month = prev_month(mydate)
    n_month = next_month(mydate)

    context = {
        'calendar':html_cal, 'prev_month':p_month, 'next_month':n_month,
        'events':events
    }
    return render(request, 'accounts/pages/calendar.html', context)


