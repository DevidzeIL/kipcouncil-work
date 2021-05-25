from django.contrib.auth import decorators
import django_filters

from django_filters import CharFilter

from django.contrib.auth.models import User

from .models import (
    Tag, Specialty, Company, Student, ListDirection, UserAward,
    Event, Member, New, About, More, DocsCollege, DocsCouncil
)



class MemberEventFilter(django_filters.FilterSet):
    class Meta: 
        model = Event
        fields = ['tags']

class MemberFilter(django_filters.FilterSet):
    class Meta: 
        model = Member
        fields = ['event']





class AdminEventMemberFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['tags']

class AdminMemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = ['user', 'event', 'role']

class AdminUserFilter(django_filters.FilterSet):
    class Meta:
        model = ListDirection
        fields = ['tags', 'status', 'user']





class NewsFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')
	text = CharFilter(field_name='text', lookup_expr='icontains')
	class Meta:
		model = New
		fields = ['tags', 'name', 'text']



class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['tags']









# .......................

class UserFilter(django_filters.FilterSet):
	email = CharFilter(field_name='email', lookup_expr='icontains')
	class Meta:
		model = User
		fields = ['email']

class StudentFilter(django_filters.FilterSet):
	fio = CharFilter(field_name='fio', lookup_expr='icontains')
	phone = CharFilter(field_name='phone', lookup_expr='icontains')
	class Meta:
		model = Student
		fields = ['group', 'fio', 'phone']

class TagFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')
	class Meta:
		model = Student
		fields = ['name']

class ListDirectionFilter(django_filters.FilterSet):
	class Meta:
		model = ListDirection
		fields = '__all__'

class UserAwardFilter(django_filters.FilterSet):
	description = CharFilter(field_name='description', lookup_expr='icontains')
	class Meta:
		model = UserAward
		fields = ['user', 'description']

class EventsFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')
	class Meta:
		model = Event
		fields = '__all__'

class CompanyFilter(django_filters.FilterSet):
	group_number = CharFilter(field_name='group_number', lookup_expr='icontains')
	class Meta:
		model = Company
		fields = '__all__'

class MembersFilter(django_filters.FilterSet):
	role = CharFilter(field_name='role', lookup_expr='icontains')
	class Meta:
		model = Member
		fields = '__all__'

class NewFilter(django_filters.FilterSet):
	name = CharFilter(field_name='name', lookup_expr='icontains')
	main_text = CharFilter(field_name='main_text', lookup_expr='icontains')
	text = CharFilter(field_name='text', lookup_expr='icontains')
	class Meta:
		model = New
		fields = ['tags', 'event', 'name', 'main_text', 'text']

class AboutFilter(django_filters.FilterSet):
	goals = CharFilter(field_name='goals', lookup_expr='icontains')
	main_text = CharFilter(field_name='main_text', lookup_expr='icontains')
	common_text = CharFilter(field_name='common_text', lookup_expr='icontains')
	result = CharFilter(field_name='result', lookup_expr='icontains')
	class Meta:
		model = About
		fields = '__all__'

class MoreFilter(django_filters.FilterSet):
	goals = CharFilter(field_name='goals', lookup_expr='icontains')
	main_text = CharFilter(field_name='main_text', lookup_expr='icontains')
	text = CharFilter(field_name='common_text', lookup_expr='icontains')
	class Meta:
		model = More
		fields = '__all__'

class DocsCollegeFilter(django_filters.FilterSet):
	description = CharFilter(field_name='description', lookup_expr='icontains')
	class Meta:
		model = DocsCollege
		fields = ['name', 'specialty', 'cource', 'description']

class DocsCouncilFilter(django_filters.FilterSet):
	description = CharFilter(field_name='description', lookup_expr='icontains')
	class Meta:
		model = DocsCouncil
		fields = ['tag', 'name', 'description']