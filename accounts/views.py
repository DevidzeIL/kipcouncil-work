from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta, date
import calendar

from django.contrib.auth.models import User

from django.utils.html import mark_safe

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import (
    Tag, Specialty, Company, Student, ListDirection, UserAward,
    Event, Member, New, About, More, DocsCollege, DocsCouncil
)

from .forms import (
    CreateUserForm, StudentForm, AwardForm,
    ListDirectionForm, UserAwardForm, EventForm, MemberForm, NewForm, 
    AboutForm, MoreForm, DocsCollegeForm, DocsCouncilForm, CompanyForm, TagForm
)

from .filters import (
    MemberEventFilter, MemberFilter, 
    AdminEventMemberFilter, AdminMemberFilter, AdminUserFilter, 
    NewsFilter, EventFilter,
    UserFilter, StudentFilter, TagFilter, ListDirectionFilter, UserAwardFilter, EventsFilter, CompanyFilter, 
    MembersFilter, NewFilter, AboutFilter, MoreFilter, DocsCollegeFilter, DocsCouncilFilter
)

from .decorators import authenticated_user, unauthenticated_user, allowed_users, admin_only
from .utils import Calendar






# Регистрация

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, username + ' был зарегистрирован!')

            return redirect('main_user')

    context = {
        'form':form
    }
    return render(request, 'accounts/auth/register.html', context)


# Вход
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
            messages.info(request, 'Email или пароль указан неверно')

    context = {}
    return render(request, 'accounts/auth/login.html', context)

# Выход
@authenticated_user
def logoutUser(request):
    logout(request)
    return redirect('main')

# 404 Страница
def error404(request):
   return render(request, 'accounts/pages/404.html')





# Начальная странциа аккаунта пользователя
@authenticated_user
def mainUser(request):
    user = request.user.student

    info = Student.objects.filter(fio = user)
    tags = Tag.objects.all()

    events_count = []
    events_member_count = []
    for tag in tags:
        events_count.append(
            Event.objects.filter(tags__name=tag.name).count()
        )
        events_member_count.append(
            request.user.student.member_set.filter(event__tags__name=tag.name).count()
        )

    awards = request.user.student.useraward_set.all().order_by('-date_created')
    
    context = {
        'info':info,
        'user':user, 'tags':tags, 'awards':awards,
        'events_count': events_count, 'events_member_count':events_member_count,
    }

    return render(request, 'accounts/auth/user.html', context)

# ПОЛЬЗОВАТЕЛЬ Выгрузка записей из БД Участников мероприятий конкретного пользователя
@authenticated_user
def userTable(request, pk_test):
    events = Event.objects.all()
    members = Member.objects.filter(user__id = pk_test)
    
    myEventFilter = MemberEventFilter(request.GET, queryset = events)
    myMemberFilter = MemberFilter(request.GET, queryset = members)
    
    events = myEventFilter.qs
    members = myMemberFilter.qs

    context = {
        'events':events, 'members':members,
        'myEventFilter':myEventFilter, 'myMemberFilter':myMemberFilter
        
    }
    return render(request, 'accounts/auth/user_table.html', context)

# Настройки аккаунта пользователя 
@authenticated_user
def accountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)
   
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('main_user')

        
    context = {'form':form}
    return render(request, 'accounts/auth/account_settings.html', context)





# АДМИН Выгрузка записей Мероприятий (Event) и Участников мероприятий (Member)
@authenticated_user
@admin_only
def adminTable(request):
    account = request.user.student

    events = Event.objects.all()
    members = Member.objects.all()
    
    myFilterEvent = AdminEventMemberFilter(request.GET, queryset = events)
    myFilterMember = AdminMemberFilter(request.GET, queryset = members)
    
    events = myFilterEvent.qs
    members = myFilterMember.qs
    
    context = {
        'account':account,
        'events':events, 'members':members,
        'myFilterEvent':myFilterEvent, 'myFilterMember':myFilterMember
        
    }
    return render(request, 'accounts/auth/admin_table.html', context)

# АДМИН Функция перехода на страницу пользователя 
@authenticated_user
@admin_only
def adminLookuser(request, pk_test):
    user = Student.objects.get(fio = pk_test)
    info = Student.objects.filter(fio = user)
    tags = Tag.objects.all()
    events_count = []
    events_member_count = []
    for tag in tags:
        events_count.append(
            Event.objects.filter(tags__name=tag.name).count()
        )
        events_member_count.append(
            Member.objects.filter(user = user, event__tags__name=tag.name).count()
        )
    awards = UserAward.objects.filter(user = user).order_by('-date_created')
    context = {
        'info':info,
        'user':user, 'tags':tags, 'awards':awards,
        'events_count': events_count, 'events_member_count':events_member_count,
    }

    return render(request, 'accounts/auth/admin_lookuser.html', context)



# ПОЛЬЗОВАТЕЛЬ Работа с БД (портфолио)
## ПОЛЬЗОВАТЕЛЬ Создание значений в БД
@authenticated_user
def createAward(request, pk_test):
    user = Student.objects.get(id=pk_test)
    form = AwardForm(initial={'user':user})

    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_user')

    context = {
        'form':form
    }
    return render(request, 'accounts/auth/award_form.html', context)

## ПОЛЬЗОВАТЕЛЬ Изменение значений в БД
@authenticated_user
def editAward(request, pk_test):
    award = UserAward.objects.get(id=pk_test)
    form = AwardForm(instance=award)

    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES, instance=award)
        if form.is_valid():
            form.save()
            return redirect('main_user')

    context = {
        'form':form, 'award':award
    }
    return render(request, 'accounts/auth/award_form.html', context)

## ПОЛЬЗОВАТЕЛЬ Удаление значений из БД
@authenticated_user
def deleteAward(request, pk_test):
    award = UserAward.objects.get(id=pk_test)

    if request.method == 'POST':
        award.delete()
        return redirect('main_user')

    context = {
        'award':award
    }
    return render(request, 'accounts/auth/delete_award.html', context)





## АДМИН Выгрузка записей из БД в таблицу
@authenticated_user
@admin_only
def adminTableDB(request, pk_test):
    account = request.user.student

    if (pk_test == 'Student'):
        form = Student.objects.all().order_by('group')
        myFilter = StudentFilter(request.GET, queryset = form)
        form = myFilter.qs

    elif (pk_test == 'User'):
        form = User.objects.all()
        myFilter = UserFilter(request.GET, queryset = form)
        form = myFilter.qs

    elif (pk_test == 'Tag'):
        form = Tag.objects.all()
        myFilter = TagFilter(request.GET, queryset = form)
        form = myFilter.qs

    elif (pk_test == 'ListDirection'):
        form = ListDirection.objects.all().order_by('date_created')
        myFilter = ListDirectionFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'Event'):
        form = Event.objects.all().order_by('-date')
        myFilter = EventsFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'Member'):
        form = Member.objects.all()
        myFilter = MembersFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'New'):
        form = New.objects.all().order_by('-date_created')
        myFilter = NewFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'UserAward'):
        form = UserAward.objects.all()
        myFilter = UserAwardFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'Company'):
        form = Company.objects.all()
        myFilter = CompanyFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'About'):
        form = About.objects.all()
        myFilter = AboutFilter(request.GET, queryset = form)
        form = myFilter.qs
    
    elif (pk_test == 'More'):
        form = More.objects.all()
        myFilter = MoreFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'DocsCollege'):
        form = DocsCollege.objects.all()
        myFilter = DocsCollegeFilter(request.GET, queryset = form)
        form = myFilter.qs


    elif (pk_test == 'DocsCouncil'):
        form = DocsCouncil.objects.all()
        myFilter = DocsCouncilFilter(request.GET, queryset = form)
        form = myFilter.qs


    context = {
        'form':form, 'pk_test':pk_test, 'myFilter':myFilter, 'account':account
    }
    return render(request, 'accounts/auth/admin_tabledb.html', context)

# АДМИН Работа с БД
## АДМИН Создание записи в БД
@authenticated_user
@admin_only
def adminCreateDB(request, pk_test):
    if (pk_test == 'Student'):
        form = StudentForm()
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES,)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'User'):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'Tag'):
        form = TagForm()
        if request.method == 'POST':
            form = TagForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'ListDirection'):
        form = ListDirectionForm()
        if request.method == 'POST':
            form = ListDirectionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'Event'):
        form = EventForm()
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'Member'):
        form = MemberForm()
        if request.method == 'POST':
            form = MemberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'New'):
        form = NewForm()
        if request.method == 'POST':
            form = NewForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'UserAward'):
        form = UserAwardForm()
        if request.method == 'POST':
            form = UserAwardForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'Company'):
        form = CompanyForm()
        if request.method == 'POST':
            form = CompanyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'About'):
        form = AboutForm()
        if request.method == 'POST':
            form = AboutForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)

    elif (pk_test == 'More'):
        form = MoreForm()
        if request.method == 'POST':
            form = MoreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)

    elif (pk_test == 'DocsCollege'):
        form = DocsCollegeForm()
        if request.method == 'POST':
            form = DocsCollegeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    elif (pk_test == 'DocsCouncil'):
        form = DocsCouncilForm()
        if request.method == 'POST':
            form = DocsCouncilForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test)


    context = {
        'form':form, 'pk_test':pk_test
    }
    return render(request, 'accounts/auth/admin_workdb.html', context)

## АДМИН Изменение записи из БД
@authenticated_user
@admin_only
def adminEditDB(request, pk_test1, pk_test2): 
    if (pk_test1 == 'Student'):
        item = Student.objects.get(id=pk_test2)
        form = StudentForm(instance=item)
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)
    
    elif (pk_test1 == 'User'):
        item = User.objects.get(id=pk_test2)
        form = CreateUserForm(instance=item)
        if request.method == 'POST':
            form = CreateUserForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)

    elif (pk_test1 == 'Tag'):
        item = Tag.objects.get(id=pk_test2)
        form = TagForm(instance=item)
        if request.method == 'POST':
            form = TagForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'ListDirection'):
        item = ListDirection.objects.get(id=pk_test2)
        form = ListDirectionForm(instance=item)
        if request.method == 'POST':
            form = ListDirectionForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'Event'):
        item = Event.objects.get(id=pk_test2)
        form = EventForm(instance=item)
        if request.method == 'POST':
            form = EventForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'Member'):
        item = Member.objects.get(id=pk_test2)

        form = MemberForm(instance=item)
        if request.method == 'POST':
            form = MemberForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'New'):
        item = New.objects.get(id=pk_test2)

        form = NewForm(instance=item)
        if request.method == 'POST':
            form = NewForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'UserAward'):
        item = UserAward.objects.get(id=pk_test2)

        form = UserAwardForm(instance=item)
        if request.method == 'POST':
            form = UserAwardForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'Company'):
        item = Company.objects.get(id=pk_test2)

        form = CompanyForm(instance=item)
        if request.method == 'POST':
            form = CompanyForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)

    elif (pk_test1 == 'About'):
        item = About.objects.get(id=pk_test2)

        form = AboutForm(instance=item)
        if request.method == 'POST':
            form = AboutForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)

    elif (pk_test1 == 'More'):
        item = More.objects.get(id=pk_test2)

        form = MoreForm(instance=item)
        if request.method == 'POST':
            form = MoreForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'DocsCollege'):
        item = DocsCollege.objects.get(id=pk_test2)

        form = DocsCollegeForm(instance=item)
        if request.method == 'POST':
            form = DocsCollegeForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)


    elif (pk_test1 == 'DocsCouncil'):
        item = DocsCouncil.objects.get(id=pk_test2)

        form = DocsCouncilForm(instance=item)
        if request.method == 'POST':
            form = DocsCouncilForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('admin_tabledb', pk_test1)



    context = {
        'form':form, 'pk_test':pk_test1
    }
    return render(request, 'accounts/auth/admin_workdb.html', context)

## АДМИН Удаление записи из БД
@authenticated_user
@admin_only
def adminDeleteDB(request, pk_test1, pk_test2):   
    if (pk_test1 == 'Student'):
        item = Student.objects.get(id=pk_test2)
    elif (pk_test1 == 'User'):
        item = User.objects.get(id=pk_test2)
    elif (pk_test1 == 'Tag'):
        item = Tag.objects.get(id=pk_test2)
    elif (pk_test1 == 'ListDirection'):
        item = ListDirection.objects.get(id=pk_test2)
    elif (pk_test1 == 'Event'):
        item = Event.objects.get(id=pk_test2)
    elif (pk_test1 == 'Member'):
        item = Member.objects.get(id=pk_test2)
    elif (pk_test1 == 'New'):
        item = New.objects.get(id=pk_test2)
    elif (pk_test1 == 'UserAward'):
        item = UserAward.objects.get(id=pk_test2)
    elif (pk_test1 == 'Company'):
        item = Company.objects.get(id=pk_test2)
    elif (pk_test1 == 'About'):
        item = About.objects.get(id=pk_test2)
    elif (pk_test1 == 'More'):
        item = More.objects.get(id=pk_test2)
    elif (pk_test1 == 'DocsCollege'):
        item = DocsCollege.objects.get(id=pk_test2)
    elif (pk_test1 == 'DocsCouncil'):
        item = DocsCouncil.objects.get(id=pk_test2)

    if request.method == 'POST':
        item.delete()
        return redirect('admin_tabledb', pk_test1)

    context = {
        'item':item, 'pk_test1':pk_test1
    }
    return render(request, 'accounts/auth/admin_deletedb.html', context)






def main(request):
    event_all = New.objects.all().last()
    more = More.objects.all()

    tags = Tag.objects.all()
    posts = []
    for tag in tags:
        posts.append(
            New.objects.filter(tags=tag).last()
        )
        
    context = {
        'event_all':event_all, 'posts':posts, 'tags':tags, 'more':more
    }
    return render(request, 'accounts/pages/home.html', context)

def direction(request, tags):
    news = New.objects.filter(tags=tags)
    users = ListDirection.objects.filter(tags=tags)
    text_about = About.objects.filter(tags=tags).last()

    context = {
    'news':news, 'users':users, 'text_about':text_about
    }
    return render(request, 'accounts/pages/direction.html', context)

def about(request):
    users = ListDirection.objects.filter(status="Правление")
    text_about = About.objects.filter(tags__name="Общее").last()

    account = None

    if unauthenticated_user != True:
        account = request.user.student

    context = {
        'users':users, 'text_about':text_about, 'account':account
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

def news(request):
    news_list = New.objects.all().order_by('date_created')
    myFilter = NewsFilter(request.GET, queryset = news_list)
    news_list = myFilter.qs

    context = {
        'news_list':news_list, 'myFilter':myFilter
    }
    return render(request, 'accounts/pages/news.html', context)

def news_about(request, pk_test):
    new = New.objects.get(id=pk_test)
    event = new.event
    members = Member.objects.filter(event = new.event)

    account = None

    if unauthenticated_user == True:
        account = request.user.student

   

    context = {
        'members':members, 'new':new, 'event':event, 'account':account
    }
    return render(request, 'accounts/pages/news_about.html', context)

def more(request, pk_test):
    field = More.objects.get(id=pk_test)

    context = {
        'field':field
    }
    return render(request, 'accounts/pages/more.html', context)




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

    myFilter = EventFilter(request.GET, queryset = events)

    context = {
        'calendar':html_cal, 'prev_month':p_month, 'next_month':n_month,
        'myFilter':myFilter, 'events':events
    }
    return render(request, 'accounts/pages/calendar.html', context)





def secret(request):
   return render(request, 'accounts/pages/secret.html')
