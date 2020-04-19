from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(redirect_authenticated_user=True),
         name='login'),
    path('accounts/signup/', views.SignUp, name='signup'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout', kwargs={'next_page': '/'}),
]
