from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profileEdit', views.profileEdit, name='profileEdit'),
    path('profile', views.profile, name='profile'),
    path('instructions', views.instructions, name='instructions'),
    path('sampleTest', views.sample_test, name='sampletest'),
    path('feedback', views.feedback, name='feedback'),

]