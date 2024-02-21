"""GMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gym import views as admin_view
from gym_web import views as web_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',Home, name='home'),
    path('web/',web_view.gym_web_index, name='gym_web_index'),
    path('contact/',web_view.gym_web_contact, name='gym_web_contact'),
    path('about/',web_view.gym_web_about, name='gym_web_about'),
    path('service/',web_view.gym_web_service, name='gym_web_service'),
    path('team/',web_view.gym_web_team, name='gym_web_team'),
    
    
    # path('about/',About, name = 'about'),
    # path('contact/',Contact, name = 'contact'),
    # path('admin_login',Login, name='login'),
    # path('logout/',Logout, name='logout'),

    # path('add_enquiry/',Add_Enquiry,name='add_enquiry'),
    # path('view_enquiry/',View_Enquiry,name='view_enquiry'),
    # path('delete_enquiry(?p<int:pid>)', Delete_Enquiry, name='delete_enquiry'),

    # path('add_equipment/',Add_Equipment,name='add_equipment'),
    # path('view_equipment/',View_Equipment,name='view_equipment'),
    # path('delete_equipment(?p<int:pid>)', Delete_Equipment, name='delete_equipment'),

    # path('add_plan/',Add_Plan,name='add_plan'),
    # path('view_plan/',View_Plan,name='view_plan'),
    # path('delete_plan(?p<int:pid>)', Delete_Plan, name='delete_plan'),

    # path('add_member/',Add_Member,name='add_member'),
    # path('view_member/',View_Member,name='view_member'),
    # path('delete_member(?p<int:pid>)', Delete_Member, name='delete_member'),
]
 