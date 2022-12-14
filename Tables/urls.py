from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path("home",views.home,name ="home"),
    path('leaves/<int:pro>/',views.leaves,name ="leaves"),
    path('application/<int:pro>/',views.application,name ="application"),
    path('application/<int:pro>/application',views.application,name ="application"),
    path('show/<int:pro>/',views.show,name ="show"),
    path('logout/<int:pro>/',views.logout,name ="logout"),
    path('status/<int:pro>/',views.status,name ="status"),
    path('status/<int:pro>/status',views.status,name ="status"),
    path('changecsehod/<int:pro>/',views.changecsehod,name ="changecsehod"),
    path('changecsehod/<int:pro>/changecsehod',views.changecsehod,name ="changecsehod"),
    path('changeeehod/<int:pro>/',views.changeeehod,name ="changeeehod"),
    path('changeeehod/<int:pro>/changeeehod',views.changeeehod,name ="changeeehod"),
    path('changemechod/<int:pro>/',views.changemechod,name ="changemechod"),
    path('changemechod/<int:pro>/changemechod',views.changemechod,name ="changemechod"),
    path('changedean/<int:pro>/',views.changedean,name ="changedean"),
    path('changedean/<int:pro>/changedean',views.changedean,name ="changedean"),
    path('intro/<int:pro>/',views.intro,name ="intro"),
    path('intro/<int:pro>/intro',views.intro,name ="intro"),
    path('profile/<int:pro>/',views.profile,name ="profile"),
    path('profile/<int:pro>/profile',views.profile,name ="profile"),
    path('changeineducation/<int:pro>/',views.changeineducation,name = 'changeineducation'),
    path('changeincourse/<int:pro>/',views.changeincourse,name = 'changeincourse'),
    path('deleteineducation/<int:pro>/',views.deleteineducation,name = 'deleteineducation'),
    path('deleteincourse/<int:pro>/',views.deleteincourse,name = 'deleteincourse'),
    path('profile/<int:pro>/changeineducation',views.changeineducation,name ='changeineducation'),
    path('profile/<int:pro>/changeincourse',views.changeincourse,name ='changeincourse'),
    path('profile/<int:pro>/deleteineducation',views.deleteineducation,name ='deleteineducation'),
    path('profile/<int:pro>/deleteincourse',views.deleteincourse,name ='deleteincourse'),
]
