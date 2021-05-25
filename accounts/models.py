from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField



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
    phone       = models.CharField(max_length=200, null=True)
    birthday    = models.DateField(null=True)
    profile_pic = models.ImageField(default='avatar.png', null=True, blank=True)
    vk_url      = models.CharField(max_length=200, blank=True, null=True)
    instagram_url   = models.CharField(max_length=200, blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.fio)



class ListDirection(models.Model):
    STATUS = (
            ('Участник', 'Участник'),
            ('Правление', 'Правление')
    )

    tags        = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    user        = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    status      = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
    role        = models.CharField(max_length=200, blank=True, null=True) 
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.fio
        


class UserAward(models.Model):
    user        = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    award       = models.ImageField(default='avatar.png', null=True, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)



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
    main_text   = RichTextField(max_length=300, blank=True, null=True)
    text        = RichTextField(max_length=1000, blank=True, null=True)
    link        = models.CharField(max_length=200, blank=True, null=True)
    photo       = models.ImageField(default='rec.png', null=True, blank=True)
    date_created     = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class About(models.Model):
    tags        = models.ForeignKey(Tag, null = True, blank = True, on_delete = models.SET_NULL)
    goals       = RichTextField(max_length=200, blank=True, null=True)
    main_text   = RichTextField(max_length=300, blank=True, null=True)
    text        = RichTextField(max_length=1000, blank=True, null=True)
    result      = RichTextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.tags.name


class More(models.Model):
    tags        = models.ForeignKey(Tag, null = True, blank = True, on_delete = models.SET_NULL)
    name        = models.CharField(max_length=200,  blank=True, null=True)
    goals       = RichTextField(max_length=200, blank=True, null=True)
    main_text   = RichTextField(max_length=300, blank=True, null=True)
    text        = RichTextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.tags.name



class DocsCollege(models.Model):
    COURCE = (
            ('1 курс', '1 курс'),
            ('2 курс', '2 курс'),
            ('3 курс', '3 курс'),
            ('4 курс', '4 курс')
    )
    name        = models.CharField(max_length=200, null=True, blank=True)
    file        = models.FileField(null=True, blank=True)
    specialty   = models.ForeignKey(Specialty, null = True, blank = True, on_delete = models.SET_NULL)
    cource      = models.CharField(max_length=200, null=True,  blank = True,choices=COURCE)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class DocsCouncil(models.Model):
    tag         = models.ForeignKey(Tag, null = True, blank = True, on_delete = models.SET_NULL)
    file        = models.FileField(null=True, blank=True)
    name        = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name