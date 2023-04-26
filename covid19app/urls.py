from django.urls import path
from .views import(CreateRecords, ViewRecords, DeleteRecords)


urlpatterns = [
    path("CreateRecord/", CreateRecords.as_view(), name='create_record'),
    path("ViewRecord/", ViewRecords.as_view(), name='view_record'),
    path("DeleteRecord/<int:pk>/", DeleteRecords.as_view(), name='delete_record')


]