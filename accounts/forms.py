from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import (
    ListDirection, Student, Tag, UserAward,
    Event, Member, New,
    DocsCollege, DocsCouncil
)



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['user']

class AwardForm(ModelForm):
	class Meta:
		model = UserAward
		fields = '__all__'


class AddTagForm(ModelForm):
	class Meta:
		model = Tag
		fields = ['name']

class AddUserForm(ModelForm):
	class Meta:
		model = ListDirection
		fields = ['user', 'tags', 'status', 'role']

class AddEventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'

class AddMemberForm(ModelForm):
	class Meta:
		model = Member
		fields = ['event', 'user', 'role', 'comment']

class AddNewForm(ModelForm):
	class Meta:
		model = New
		fields = '__all__'