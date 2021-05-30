from django.urls import path
from . views import QuizListView,quiz_view,find_result,quiz_data_view


app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz_view'),
    path('<pk>/save/', find_result, name = "find_result"),
    path('<pk>/data/', quiz_data_view, name='quiz_data_view'),
]