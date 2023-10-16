from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.displayQuestionView.as_view(), name='display'),
    path("<int:pk>/", views.DetailQuestionView.as_view() ,name='detail'),
    path("<int:pk>/result/", views.ResultOfVote.as_view() , name='result'),
    path("<int:question_id>/vote", views.vote, name='vote'),

]