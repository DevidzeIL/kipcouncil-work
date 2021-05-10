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
    Specialty, Company, Student, UserFunction, UserAward, UserComment, 
    Tag, Event, Member, New, About, 
    DocsName, DocsCollege, DocsCouncil
)

from .forms import CreateUserForm, StudentForm, AwardForm
from .filters import MemberFilter, AdminFilter
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
    user = request.user.student

    tags = Tag.objects.all()

    events = []
    events_member = []
    for tag in tags:
        events.append(
            Event.objects.filter(tags__name=tag.name).count()
        )
        events_member.append(
            request.user.student.member_set.filter(event__tags__name=tag.name).count()
        )

    event_procents = []
    for i in range(0, len(events)):
        event_procents.append(events_member[i] * 100 / events[i])


    awards = request.user.student.useraward_set.all()

    context = {
        'user':user, 'tags':tags, 'awards':awards,
        'events': events, 'events_member':events_member,
        'event_procents':event_procents,
    }

    return render(request, 'accounts/auth/user.html', context)



def createAward(request, pk_test):
    user = Student.objects.get(id=pk_test)
    form = AwardForm(initial={'user':user})

    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-page')

    context = {
        'form':form
    }
    return render(request, 'accounts/auth/award_form.html', context)

def editAward(request, pk_test):
    award = UserAward.objects.get(id=pk_test)
    form = AwardForm(instance=award)

    if request.method == 'POST':
        form = AwardForm(request.POST, instance=award)
        if form.is_valid():
            form.save()
            return redirect('user-page')

    context = {
        'form':form
    }
    return render(request, 'accounts/auth/award_form.html', context)

def deleteAward(request, pk_test):
    award = UserAward.objects.get(id=pk_test)


    if request.method == 'POST':
        award.delete()
        return redirect('user-page')

    context = {
        'award':award
    }
    return render(request, 'accounts/auth/delete_award.html', context)



def userTable(request, pk_test):
    events = Event.objects.all()
    members = Member.objects.filter(user__id = pk_test)

    myFilter = MemberFilter(request.GET, queryset = members)

    members = myFilter.qs

    context = {
        'events':events, 'members':members,
        'myFilter':myFilter
        
    }
    return render(request, 'accounts/auth/user_table.html', context)



def adminTable(request):
    events = Event.objects.all()
    members = Member.objects.all()

    myFilter = AdminFilter(request.GET, queryset = members)

    members = myFilter.qs

    context = {
        'events':events, 'members':members,
        'myFilter':myFilter
        
    }
    return render(request, 'accounts/auth/admin_table.html', context)

def adminLookuser(request, pk_test):
    user = Student.objects.get(fio = pk_test)

    tags = Tag.objects.all()

    events = []
    events_member = []
    for tag in tags:
        events.append(
            Event.objects.filter(tags__name=tag.name).count()
        )
        events_member.append(
            Member.objects.filter(user = user, event__tags__name=tag.name).count()
        )

    event_procents = []
    for i in range(0, len(events)):
        event_procents.append(events_member[i] * 100 / events[i])


    awards = UserAward.objects.filter(user = user)
    context = {
        'user':user, 'tags':tags, 'awards':awards,
        'events': events, 'events_member':events_member,
        'event_procents':event_procents,
    }

    return render(request, 'accounts/auth/admin_lookuser.html', context)



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
    event_all = Event.objects.all().last()

    tags = Tag.objects.all()
    posts = []
    for tag in tags:
        posts.append(
            New.objects.filter(tags=tag).last()
        )
        
    context = {
        'event_all':event_all, 'posts':posts, 'tags':tags
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
    specialties = Specialty.objects.all()
    cources = ["1 курс", "2 курс", "3 курс", "4 курс"]
    docs = DocsCollege.objects.all()

    context = {
        'specialties':specialties, 'cources':cources, 'docs':docs
    }
    return render(request, 'accounts/pages/docs_college.html', context)



def docs_council(request):
    tags = Tag.objects.all()
    docs = DocsCouncil.objects.all()

    context = {
        'tags':tags, 'docs':docs
    }
    return render(request, 'accounts/pages/docs_council.html', context)



def news_about(request, pk_test):
    new = New.objects.get(id=pk_test)
    event = new.event
    members = Member.objects.filter(event = new.event)

    context = {
        'members':members, 'new':new, 'event':event
    }
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


