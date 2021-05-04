from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Student

def student_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)
        Student.objects.create(
                user = instance,
                email = instance.email,
                fio = instance.username
            )
        print('Profile created')

post_save.connect(student_profile, sender=User)