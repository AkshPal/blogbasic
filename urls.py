   
from django.urls import path , include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile"),
    path("Login/",views.Login,name="Login"),
    path("blogs/",views.blogs,name="blogs"),
    path("addblogs/",views.addblogs,name="addblogs"),
    path("blog_comments",views.blogs_comments,name="blog_comments"),   
    path("Logout", views.Logout, name= "Logout"),
    path("about/",views.about,name="about"),
]
