# Представления
Представления в Django —это то, что в классическом паттерне MVC называется контроллерами. Это место, где происходит обработка запросов и формирование ответов. Они определяются в файле views.py.

В рамках данной лабораторной работы структура этого файла следующая:

``` Python
# *** пока что представления только с rest api ***


from projects.models import File, ProjectTopic, Project, GradeReport, \
ProjectOfUser, Teacher, Student, Grade, ProjectMeeting, Meeting
from projects.serializers import *

from rest_framework import generics, permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешение только для владельца объекта на редактирование.
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешить любые безопасные (например, GET) запросы.
        return obj.owner == request.user  # Здесь obj.owner - это поле, содержащее владельца объекта.

# File
class FileListAPIView(generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class FileDestroyAPIView(generics.DestroyAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class FileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class FileCreateAPIView(generics.CreateAPIView):
   serializer_class = FileSerializer
   queryset = File.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# ProjectTopic
class ProjectTopicListAPIView(generics.ListAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ProjectTopicDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectTopicUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectTopicCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectTopicSerializer
   queryset = ProjectTopic.objects.all()
   permission_classes = [permissions.IsAdminUser] # TODO

# Project
class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer # ProjectDepthSerializer TODO:
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectSerializer
   queryset = Project.objects.all()
   permission_classes = [permissions.IsAdminUser]

# GradeReport
class GradeReportListAPIView(generics.ListAPIView):
    serializer_class = GradeReportSerializer # TODO: GradeReportDepthSerializer
    queryset = GradeReport.objects.all()
    permission_classes = [permissions.IsAdminUser]

class GradeReportDestroyAPIView(generics.DestroyAPIView):
    serializer_class = GradeReportSerializer
    queryset = GradeReport.objects.all()
    permission_classes = [permissions.IsAdminUser]

class GradeReportUpdateAPIView(generics.UpdateAPIView):
    serializer_class = GradeReportSerializer
    queryset = GradeReport.objects.all()
    permission_classes = [permissions.IsAdminUser]

class GradeReportCreateAPIView(generics.CreateAPIView):
   serializer_class = GradeReportSerializer
   queryset = GradeReport.objects.all()
   permission_classes = [permissions.IsAdminUser]

# ProjectOfUser
class ProjectOfUserListAPIView(generics.ListAPIView):
    serializer_class = ProjectOfUserSerializer # TODO: ProjectOfUserDepthSerializer
    queryset = ProjectOfUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectOfUserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectOfUserSerializer
    queryset = ProjectOfUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectOfUserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectOfUserSerializer
    queryset = ProjectOfUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectOfUserCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectOfUserSerializer
   queryset = ProjectOfUser.objects.all()
   permission_classes = [permissions.IsAdminUser]

# Teacher
class TeacherListAPIView(generics.ListAPIView):
    serializer_class = TeacherSerializer # TODO: TeacherDepthSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TeacherDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAdminUser]

class TeacherUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAdminUser]

class TeacherCreateAPIView(generics.CreateAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()
   permission_classes = [permissions.IsAdminUser]

# Student
class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer # TODO: StudentDepthSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class StudentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAdminUser]

class StudentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAdminUser]

class StudentCreateAPIView(generics.CreateAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()
   permission_classes = [permissions.IsAdminUser]

# Grade
class GradeListAPIView(generics.ListAPIView):
    serializer_class = GradeSerializer # TODO: GradeDepthSerializer
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class GradeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class GradeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class GradeCreateAPIView(generics.CreateAPIView):
   serializer_class = GradeSerializer
   queryset = Grade.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# ProjectMeeting
class ProjectMeetingListAPIView(generics.ListAPIView):
    serializer_class = ProjectMeetingSerializer # TODO: ProjectMeetingDepthSerializer
    queryset = ProjectMeeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class ProjectMeetingDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectMeetingSerializer
    queryset = ProjectMeeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class ProjectMeetingUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectMeetingSerializer
    queryset = ProjectMeeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class ProjectMeetingCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectMeetingSerializer
   queryset = ProjectMeeting.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# Meeting
class MeetingListAPIView(generics.ListAPIView):
    serializer_class = MeetingSerializer # TODO: MeetingDepthSerializer
    queryset = Meeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class MeetingDestroyAPIView(generics.DestroyAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class MeetingUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class MeetingCreateAPIView(generics.CreateAPIView):
   serializer_class = MeetingSerializer
   queryset = Meeting.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

```