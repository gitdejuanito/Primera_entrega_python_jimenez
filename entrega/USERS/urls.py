

from django.urls import path
from USERS.views import login_view, register_view,update_view,about_me
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path("login/",login_view, name='login'),
   
   path("logout/",LogoutView.as_view(template_name="logout.html")),
   path("register/",register_view),
   path("update/",update_view, name="update"),
   path("about/",about_me, name="about"),
] 
 