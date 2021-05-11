import django_filters

from .models import (
    ListDirection, Specialty, Company, Student, UserFunction, UserAward, UserComment, 
    Tag, Event, Member, New, About, 
    DocsName, DocsCollege, DocsCouncil
)


class MemberFilter(django_filters.FilterSet):
    class Meta: 
        model = Member
        fields = '__all__'
        exclude = ['user']


class AdminMemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = '__all__'

class AdminUserFilter(django_filters.FilterSet):
    class Meta:
        model = ListDirection
        fields = '__all__'


class NewsFilter(django_filters.FilterSet):
    class Meta:
        model = New
        fields = ['tags', 'event', 'name', 'date_performance']

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['tags']
