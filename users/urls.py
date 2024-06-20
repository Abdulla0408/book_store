from django.urls import path
from .views import (CategoryView, LoginView, RegisterView, ProfileView, EditProfileView,
                    DashboardView, LogoutView, ClientSignUpView, BooksDetailView, CartDetailView,
                    UsersListView, SelectRoleView, user_delete)

app_name = 'users'

urlpatterns = [
    path('category/<int:id>/', CategoryView.as_view(), name='category'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('signup/', ClientSignUpView.as_view(), name='signup'),
    path('batafsil/<int:book_id>/', BooksDetailView.as_view(), name='batafsil'),
    path('cart/', CartDetailView.as_view(), name='cart'),

    path('users-list/', UsersListView.as_view(), name='users_list'),
    path('select-role/', SelectRoleView.as_view(), name='select_role'),
    path('user-delete/<int:id>', user_delete, name='user_delete'),


]