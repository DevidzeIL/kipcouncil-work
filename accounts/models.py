from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name        = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name        = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Company(models.Model):
    COURCE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4')
    )
    сourse      = models.CharField(max_length=200, null=True, choices=COURCE)
    specialty   = models.ForeignKey(Specialty, null=True, on_delete=models.SET_NULL)
    group_number= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.group_number
     


class Student(models.Model):
    user        = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    group       = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    fio         = models.CharField(max_length=200, null=True)
    email       = models.CharField(max_length=200, null=True)
    phone       = models.CharField(max_length=200, null=True)
    birthday    = models.DateField(null=True)
    profile_pic = models.ImageField(default='avatar.png', null=True, blank=True)
    SEX = (
            ('М', 'М'),
            ('Ж', 'Ж')
    )
    sex         = models.CharField(max_length=200, null=True, choices=SEX)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fio

class ListDirection(models.Model):
    tags        = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    user        = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    role        = models.CharField(max_length=200, blank = True, null=True) 
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.fio
        

class UserFunction(models.Model):
    tags        = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    user        = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    function    = models.CharField(max_length=200, null=True)  

    def __str__(self):
        return self.user.fio



class UserAward(models.Model):
    user        = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    award       = models.ImageField(default='avatar.png', null=True, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_performance = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.user.fio


class UserComment(models.Model):
    user        = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    comment     = models.CharField(max_length=200, null=True)


class Event(models.Model):
    tags        = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    name        = models.CharField(max_length=200, null=True)
    date        = models.DateField(null=True)

    def __str__(self):
        return self.name

    @property
    def get_html_url(self):
        return f'<p>{self.name}</p><a href="{url}"></a>'



class Member(models.Model):
    user        = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    event       = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    role        = models.CharField(max_length=200, blank = True, null=True) 
    comment     = models.CharField(max_length=200, blank = True, null=True) 

    def __str__(self):
        return self.user.fio



class New(models.Model):
    tags        = models.ForeignKey(Tag, null = True, blank = True, on_delete = models.SET_NULL)
    event       = models.ForeignKey(Event, blank=True, null=True, on_delete=models.SET_NULL)
    name        = models.CharField(max_length=200,  blank=True, null=True)
    main_text   = models.CharField(max_length=300, blank=True, null=True)
    common_text = models.CharField(max_length=700, blank=True, null=True)
    third_text  = models.CharField(max_length=700, blank=True, null=True)
    link        = models.CharField(max_length=200, blank=True, null=True)
    photo       = models.ImageField(default='rec.png', null=True, blank=True)
    date_performance = models.DateField(blank=True, null=True)
    date_created     = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    tags        = models.ForeignKey(Tag, null = True, blank = True, on_delete = models.SET_NULL)
    goals       = models.CharField(max_length=200, blank=True, null=True)
    main_text   = models.CharField(max_length=200, blank=True, null=True)
    common_text = models.CharField(max_length=200, blank=True, null=True)
    result      = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.tags.name


class DocsName(models.Model):
    name        = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class DocsCollege(models.Model):
    COURCE = (
            ('1 курс', '1 курс'),
            ('2 курс', '2 курс'),
            ('3 курс', '3 курс'),
            ('4 курс', '4 курс')
    )
    name        = models.ForeignKey(DocsName, null = True, blank = True, on_delete = models.SET_NULL)
    specialty   = models.ForeignKey(Specialty, null = True, blank = True, on_delete = models.SET_NULL)
    cource      = models.CharField(max_length=200, null=True,  blank = True,choices=COURCE)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name.name


class DocsCouncil(models.Model):
    tag         = models.ForeignKey(Tag, null = True, blank = True, on_delete = models.SET_NULL)
    name        = models.ForeignKey(DocsName, null = True, blank = True, on_delete = models.SET_NULL)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name.name