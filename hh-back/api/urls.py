from django.urls import path
from api import views
from api.views import VacancyViews, VacancyDView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', views.companies),
    path('companies/<int:id>/', views.company),
    path('companies/<int:id>/vacancies/', views.vacancies_by_company),
    path('vacancies/', VacancyViews.as_view()),
    path('vacancies/<int:id>/', VacancyDView.as_view()),
]