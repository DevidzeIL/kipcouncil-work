import django_filters

from .models import (
    Specialty, Company, Student, UserFunction, UserAward, UserComment, 
    Tag, Event, Member, New, About, 
    DocsName, DocsCollege, DocsCouncil
)


class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user']


class AdminFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = '__all__'
