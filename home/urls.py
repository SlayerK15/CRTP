from django.urls import path
from home import admin
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

    path('',views.indexView,name="home"),
    path('dashboard',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='/'),name="logout"),
    path('service_based',views.service_based,name="service_based"),
    path('product_based',views.product_based,name="product_based"),
    path('faang',views.faang,name="faang"),
    path('bigcom',views.bigcom,name="bigcom"),
    path('contact',views.contact,name="contact"),
    path('tcs/', views.tcs, name='tcs_compiler'),
    path('accenture/', views.accenture, name='Accenture_compiler'),
    path('amazon/', views.amazon, name='amazon_compiler'),
    path('cognizant/', views.cognizant, name='cognizant_compiler'),
    path('capgemini/', views.capgemini, name='capgemini_compiler'),
    path('microsoft/', views.microsoft, name='microsoft_compiler'),
    path('delloite/', views.delloite, name='delloite_compiler'),
    path('atos/', views.atos, name='atos_compiler'),
    path('ibm/', views.ibm, name='ibm_compiler'),
    path('facebook/', views.facebook, name='meta_compiler'),
    path('apple/', views.apple, name='apple_compiler'),
    path('netflix/', views.netflix, name='netflix_compiler'),
    path('google/', views.google, name='google_compiler'),
    path('infosys/', views.infosys, name='infosys_compiler'),
    path('wipro/', views.wipro, name='wipro_compiler'),
    path('tm/', views.tm, name='tm_compiler'),
    path('adobe/', views.adobe, name='adobe_compiler'),
    path('cisco/', views.cisco, name='cisco_compiler'),
    path('ey/', views.ey, name='ey_compiler'),
    path('pwc/', views.pwc, name='pwc_compiler'),
]