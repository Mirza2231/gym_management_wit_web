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
from django.urls import path
from gym import views as admin_view
from gym_web import views as web_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from gym_web.views import custom_404_view

handler404 = custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',web_view.gym_web_index, name='gym_web_index'),
    path('contact/',web_view.gym_web_contact, name='gym_web_contact'),
    path('about/',web_view.gym_web_about, name='gym_web_about'),
    path('service/',web_view.gym_web_service, name='gym_web_service'),
    path('team/',web_view.gym_web_team, name='gym_web_team'),
    path('login/',web_view.login_view, name='gym_web_login'),
    path('register/',web_view.signup, name='gym_web_register'),
    path('logout/', web_view.logout_view, name='web_logout'),
    path('changepassword/', web_view.password_change, name='change'),
    path('profile/', web_view.profile_edit, name='proedit'),
    path('booking/<int:package_id>', web_view.book_time, name='book'),
    path('booking_detail/', web_view.user_bookings, name='booking_detail'),
    
    

    
    
    # path('about/',About, name = 'about'), 
    # path('contact/',Contact, name = 'contact'),
    # path('logout/',Logout, name='logout'),

# Admin Urls

    path('admin_login/',admin_view.Login, name='adminlogin'),
    path('admin_logout/',admin_view.adminLogout, name='adminlogout'),
    
    path('admin_home/',admin_view.Home, name='home'),
    path('add_trainer/',admin_view.ad_tariner,name='add_trainer'),
    path('edit_trainer/<int:trainer_id>/',admin_view.edit_trainer, name='edit_trainer'),
    path('delete_trainer/<int:trainer_id>/delete/', admin_view.delete_trainer, name='delete_trainer'),
    path('view_trainer/<int:pk>/',admin_view.TrainerDetailView.as_view() , name='trainer_detail'),
    path('add_pcategory/',admin_view.pcategory,name='add_pcategory'),
    path('edit_pcategory/<int:pcategory_id>/',admin_view.edit_pcategory, name='edit_pcategory'),
    path('delete_pcategory/<int:pcategory_id>/delete/', admin_view.delete_pcategory, name='delete_pcategory'),
    path('view_pcategory/<int:pk>/',admin_view.PcategoryDetailView.as_view() , name='pcategory_detail'),
    path('package/',admin_view.membership_package, name='add_package'),
    path('edit_package/<int:package_id>/',admin_view.edit_package, name='edit_package'),
    path('view_package/<int:pk>/',admin_view.PackageDetailView.as_view() , name='package_detail'),
    path('delete_package/<int:package_id>/delete/', admin_view.delete_package, name='delete_package'),
    path('add_shift/', admin_view.add_shift, name='add_shift'),
    
    
    
    
    
    

    path('table/',admin_view.Table,name='table'),
    
    
    path('add_enquiry/',admin_view.Add_Enquiry,name='add_enquiry'),
    path('view_enquiry/',admin_view.View_Enquiry,name='view_enquiry'),
    path('delete_enquiry(?p<int:pid>)', admin_view.Delete_Enquiry, name='delete_enquiry'),

    path('add_equipment/',admin_view.Add_Equipment,name='add_equipment'),
    path('view_equipment/',admin_view.View_Equipment,name='view_equipment'),
    path('delete_equipment(?p<int:pid>)', admin_view.Delete_Equipment, name='delete_equipment'),

    path('add_plan/',admin_view.Add_Plan,name='add_plan'),
    
    path('view_plan/',admin_view.View_Plan,name='view_plan'),
    path('delete_plan(?p<int:pid>)', admin_view.Delete_Plan, name='delete_plan'),

    path('add_member/',admin_view.Add_Member,name='add_member'),
    path('view_member/',admin_view.View_Member,name='view_member'),
    path('delete_member(?p<int:pid>)', admin_view.Delete_Member, name='delete_member'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
