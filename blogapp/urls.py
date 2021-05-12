from .import views
from django.urls import path
app_name='blogapp'
urlpatterns=[
    path('',views.fun,name='fun'),
    path('add/',views.add_blog,name='add_blog'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]