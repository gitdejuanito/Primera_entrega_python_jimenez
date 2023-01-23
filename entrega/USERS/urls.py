

from django.urls import path
from USERS.views import login_view, register_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path("login/",login_view, name='login'),
   
   path("logout/",LogoutView.as_view(template_name="logout.html")),
   path("register/",register_view),
   
] 
 