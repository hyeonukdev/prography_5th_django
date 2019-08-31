from django.urls import path
from . import views

urlpatterns = [
    # path('',views.read, name="home"),
    path('new/',views.create, name="new"),
    path('update/<int:pk>',views.update, name="update"),
    path('delete/<int:pk>',views.delete, name="delete"),
    path('detail/<int:pk>',views.detail, name="detail"),
    path('comment_delete/<int:pk>/<int:comment_id>', views.comment_delete, name="comment_delete"),     
    path('comment_edit/<int:comment_id>', views.comment_edit, name="comment_edit"),
]
