from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('new', views.new),
    path('new/create_wish', views.create_wish),
    path('edit/<int:wish_id>', views.edit),
    path('edit/<int:wish_id>/edit_wish', views.edit_wish),
    path('delete/<int:wish_id>', views.delete_wish),
    path('granted/<int:wish_id>', views.granted_wish),
]