# Модели 
Модели в Django — это классы, которые описывают структуру данных. Они хранятся в файле models.py внутри приложения. В рамках данной лабораторной работы структура этого файла следующая:
``` Python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default='avatar.svg')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class BaseModel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # TODO: automatic creator setting

    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name    

class File(BaseModel):
    file_field = models.FileField(upload_to="users-files")

class ProjectTopic(BaseModel):
    description = models.TextField(null=True)

class Project(BaseModel):
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    topics = models.ManyToManyField('ProjectTopic', verbose_name='Темы', related_name='project_topics')

class GradeReport(BaseModel):
    projects = models.ManyToManyField('Project', verbose_name='Проекты', related_name='gradereport_projects')

class ProjectOfUser(BaseModel):
	project_field = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
	user_field = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Teacher(BaseModel):
	user_field = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Student(BaseModel): 
	user_field = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Grade(BaseModel):
	student_field = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
	project_field = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
	grade_field = models.SmallIntegerField()

class ProjectMeeting(BaseModel):
	project_field = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

class Meeting(BaseModel):
	users_one_field = models.ManyToManyField('User', verbose_name='Люди', related_name='meeting_users')
      

```