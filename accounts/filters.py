import django_filters

from .models import (
    ListDirection, Student, UserAward,
    Event, Member, New,
    DocsCollege, DocsCouncil
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





class DocsCollegeFilter(django_filters.FilterSet):
    class Meta:
        model = DocsCollege
        fields = ['description']

class DocsCouncilFilter(django_filters.FilterSet):
    class Meta:
        model = DocsCouncil
        fields = ['description']
