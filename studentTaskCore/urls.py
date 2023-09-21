from django.contrib import admin
from django.urls import path, include
from discipline.urls.disciplineUrls import disciplineUrls
from discipline.urls.studentUrls import studentUrls
from discipline.urls.taskUrls import taskUrls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(disciplineUrls)),
    path('', include(studentUrls)),
    path('', include(taskUrls)),
]
