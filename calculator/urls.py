from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register"),
    path('history/', views.history, name='history'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
    path('edit/<int:id>/', views.edit_record, name='edit_record'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("users/", views.users, name="users"),
    path("users/add/", views.add_user, name="add_user"),
    path("users/edit/<int:id>/", views.edit_user, name="edit_user"),
    path("users/delete/<int:id>/", views.delete_user, name="delete_user"),
    path("users/reset/<int:id>/", views.reset_password, name="reset_password"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),
    path(
    "change-password/",
    views.change_password,
    name="change_password"
),
 path("about/", views.about, name="about"),
]