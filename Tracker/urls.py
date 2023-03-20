from . import views
from django.contrib import admin
from django.urls import include, re_path

admin.autodiscover()

urlpatterns = [
    #Login
    re_path(r'^$',views.log, name='log'),
    re_path(r'^signup/$',views.signup,name='signup'),
    re_path(r'^authentication/$', views.login_next, name='login_next'),
    re_path(r'^home/$',views.home,name='home'),
    re_path(r'^log_end/$',views.log_end,name='logout'),
    re_path(r'^add_group/$',views.add_group, name='add_group'),
    re_path(r'^group/$',views.group, name='group'),
    #Others
    re_path(r'^add_project/$',views.add_project, name='add_project'),
    re_path(r'^search/$', views.search, name ='search'),
    #Project
    re_path(r'^edit_project/(?P<project_id>[0-9]+)/$',views.edit_project, name='edit_project'),
    re_path(r'^delete_project/(?P<project_id>[0-9]+)/$',views.delete_project, name='delete_project'),
    re_path(r'^add_task/(?P<project_id>[0-9]+)/$',views.add_task, name='add_task'),
    re_path(r'^add_sprint/(?P<project_id>[0-9]+)/$',views.add_sprint, name='add_sprint'),
    re_path(r'^search_tag/$',views.search_tag, name='search_tag'),
    re_path(r'^chart/(?P<project_id>[0-9]+)/$',views.pieview, name='chart'),
    re_path(r'^calendar/(?P<project_id>[0-9]+)/$',views.calendar, name='calendar'),
    re_path(r'^calendar1/(?P<project_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.calendar1, name='calendar1'),
    re_path(r'^calendar2/(?P<project_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.calendar2, name='calendar2'),
    #Task
    re_path(r'^tsr/(?P<task_id>[0-9]+)/(?P<sprint_id>[0-9]+)/$',views.tsr, name='tsr'),
    re_path(r'^ts/(?P<task_id>[0-9]+)/(?P<sprint_id>[0-9]+)/$',views.ts, name='ts'),
    re_path(r'^edit_task/(?P<task_id>[0-9]+)/$',views.edit_task, name='edit_task'),
    re_path(r'^delete_task/(?P<task_id>[0-9]+)/$',views.delete_task, name='delete_task'),
    #Sprint
    re_path(r'^edit_sprint/(?P<sprint_id>[0-9]+)/$',views.edit_sprint, name='edit_sprint'),
    re_path(r'^delete_sprint/(?P<sprint_id>[0-9]+)/$',views.delete_sprint, name='delete_sprint'),
    #Image
    re_path(r'^upload/(?P<project_id>[0-9]+)/', views.FileView, name='file_upload'),
    re_path(r'^files/(?P<project_id>[0-9]+)/', views.FilesList, name='files'),
    #Notifications
    re_path(r'^notifications/$',views.notifications, name='notifications'),
    ]
 
