from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Company(models.Model):
    SPECIALTY = (
            ('ПКС', 'ПКС'),
            ('ОИБАС', 'ОИБАС'),
            ('ИСИП', 'ИСИП')
    )
    
    COURCE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4')
    )
    сourse = models.CharField(max_length=200, null=True, choices=COURCE)
    specialty = models.CharField(max_length=200, null=True, choices=SPECIALTY)
    group_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.group_number
    


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    fio = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='avatar.png', null=True, blank=True)
    SEX = (
            ('М', 'М'),
            ('Ж', 'Ж')
    )
    sex = models.CharField(max_length=200, null=True, choices=SEX)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username



class UserFunction(models.Model):
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    function = models.CharField(max_length=200, null=True)  



class UserAward(models.Model):
    user = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    award = models.CharField(max_length=200, null=True)



class UserComment(models.Model):
    user = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=200, null=True)


# from django.urls import reverse
class Event(models.Model):
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)


    def __str__(self):
        return self.name

    @property
    def get_html_url(self):
        return f'<p>{self.name}</p><a href="{url}">edit</a>'



class Member(models.Model):
    user = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=200, null=True) 
    score = models.CharField(max_length=200, null=True)




class New(models.Model):
    tags = models.ManyToManyField(Tag)
    event = models.ForeignKey(Event, null = True, blank = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=200,  blank = True, null=True)
    main_text = models.CharField(max_length=200, blank = True, null=True)
    common_text = models.CharField(max_length=200, blank = True, null=True)
    link = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     members = Member.objects.filter(event=self.event)
    #     self.members.add(*members)
    #     print('SELF:::', self.members)

    # def save_related(self, request, form, formsets, change):
    #     members = Member.objects.filter(event=self.event)
    #     self.members.add(*members)
    #     super().save_related(request, form, formsets, change)
        


class About(models.Model):
    tags = models.ManyToManyField(Tag)
    goals = models.CharField(max_length=200, null=True)
    main_text = models.CharField(max_length=200, null=True)
    common_text = models.CharField(max_length=200, null=True)
    result = models.CharField(max_length=200, null=True)


class DocsCollege(models.Model):
    SPECIALTY = (
            ('ПКС', 'ПКС'),
            ('ОИБАС', 'ОИБАС'),
            ('ИСИП', 'ИСИП')
    )
    
    COURCE = (
            ('1 курс', '1 курс'),
            ('2 курс', '2 курс'),
            ('3 курс', '3 курс'),
            ('4 курс', '4 курс')
    )

    NAME = (
            ('ПРОТОКОЛ', 'ПРОТОКОЛ'),
            ('ПОЛОЖЕНИЕ', 'ПОЛОЖЕНИЕ'),
            ('ПРЕЗЕНТАЦИЯ', 'ПРЕЗЕНТАЦИЯ'),
            ('ДОКУМЕНТ', 'ДОКУМЕНТ'),
    )
    name = models.CharField(max_length=200, null=True, choices=NAME)
    specialty = models.CharField(max_length=200, null=True, choices=SPECIALTY)
    cource = models.CharField(max_length=200, null=True, choices=COURCE)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class DocsCouncil(models.Model):
    DIRECTION = (
            ('ОБЩЕЕ', 'ОБЩЕЕ'),
            ('КУЛЬТМАСС', 'КУЛЬТМАСС'),
            ('СПОРТ', 'СПОРТ'),
            ('ПРОФКА', 'ПРОФКА'),
            ('ИНФОРМ', 'ИНФОРМ'),
            ('МУЛЬТИМЕДИА', 'МУЛЬТИМЕДИА'),
            ('КРУЖКИ', 'КРУЖКИ'),
    )

    NAME = (
            ('ПРОТОКОЛ', 'ПРОТОКОЛ'),
            ('ПОЛОЖЕНИЕ', 'ПОЛОЖЕНИЕ'),
            ('ПРЕЗЕНТАЦИЯ', 'ПРЕЗЕНТАЦИЯ'),
            ('ДОКУМЕНТ', 'ДОКУМЕНТ'),
    )

    name = models.CharField(max_length=200, null=True, choices=NAME)
    direction = models.CharField(max_length=200, null=True, choices=DIRECTION)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name