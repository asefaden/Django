from django.urls import path  # type: ignore[import]
from .views import StudentList, StudentDetail # Import StudentDetail
from .views import FrameList # FrameList is now ListCreateAPIView

urlpatterns = [
    path('api/frameDataStorage', FrameList.as_view(), name='frame sets'),
    path('api/students', StudentList.as_view(), name='students'),
    path('api/students/<int:pk>', StudentDetail.as_view(), name='student-detail'), # Use pk for detail view
    # The delete and update paths are now handled by student-detail with appropriate HTTP methods
    # path('api/delete/<int:idDelete>', StudentList.as_view(), name='delete'), # Removed
    # path('api/update/<int:idUpdate>', StudentList.as_view(), name='update'), # Removed
]
# from django.urls import path
# from api import views
# from . import views

# urlpatterns = [
#     path('student/', views.StudentList.as_view(),
#          name='student read and create-data'),
#     path('delete/<int:idDelete>', views.delete_records, name='Delete records'),
#     path('update/<int:idUpdate>',
#          views.update_records, name='update records'),
# ]
