from django.urls import path
from . import views # import views from the CURRENT directory

# strict named variable urlpatterns
# register all URL for this APP

# first arg = path AFTER our domain 
# second arg = view function
urlpatterns = [
    path('meetups/', views.index) # point to function, not execute

]