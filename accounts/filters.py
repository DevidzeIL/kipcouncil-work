import django_filters

from django_filters import CharFilter

from .models import (
    Tag, Specialty, Company, Student, ListDirection, UserAward,
    Event, Member, New, About, DocsCollege, DocsCouncil
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
    class Meta:
        model = New
        fields = ['tags', 'name', 'date_performance']





class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['tags']









# .......................

class StudentFilter(django_filters.FilterSet):
	class Meta:
		model = Student
		fields = ['group']

class ListDirectionFilter(django_filters.FilterSet):
	class Meta:
		model = ListDirection
		fields = '__all__'

class UserAwardFilter(django_filters.FilterSet):
	class Meta:
		model = UserAward
		fields = ['user', 'description', 'date_performance']

class EventsFilter(django_filters.FilterSet):
	class Meta:
		model = Event
		fields = '__all__'

class CompanyFilter(django_filters.FilterSet):
	class Meta:
		model = Company
		fields = '__all__'

class MembersFilter(django_filters.FilterSet):
	class Meta:
		model = Member
		fields = '__all__'

class NewFilter(django_filters.FilterSet):
	class Meta:
		model = New
		fields = ['tags', 'event', 'name', 'date_performance']

class AboutFilter(django_filters.FilterSet):
	class Meta:
		model = About
		fields = '__all__'

class DocsCollegeFilter(django_filters.FilterSet):
	class Meta:
		model = DocsCollege
		fields = '__all__'

class DocsCouncilFilter(django_filters.FilterSet):
	class Meta:
		model = DocsCouncil
		fields = '__all__'

