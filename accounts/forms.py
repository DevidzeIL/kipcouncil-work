from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import (
    Tag, Specialty, Company, Student, ListDirection, UserAward,
    Event, Member, New, About, More, DocsCollege, DocsCouncil
)



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['email']

class AwardForm(ModelForm):
	class Meta:
		model = UserAward
		fields = '__all__'



# ---------------------------

class TagForm(ModelForm):
	class Meta:
		model = Tag
		fields = ['name']

class ListDirectionForm(ModelForm):
	class Meta:
		model = ListDirection
		fields = '__all__'

class UserAwardForm(ModelForm):
	class Meta:
		model = UserAward
		fields = '__all__'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = '__all__'

class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = '__all__'

class NewForm(ModelForm):
	class Meta:
		model = New
		fields = '__all__'

class AboutForm(ModelForm):
	class Meta:
		model = About
		fields = '__all__'

class MoreForm(ModelForm):
	class Meta:
		model = More
		fields = '__all__'

class DocsCollegeForm(ModelForm):
	class Meta:
		model = DocsCollege
		fields = '__all__'

class DocsCouncilForm(ModelForm):
	class Meta:
		model = DocsCouncil
		fields = '__all__'
