from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # Course details
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Enrollment
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Submit exam
    path('<int:course_id>/submit/', views.submit, name='submit'),

    # Show exam result
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='exam_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
