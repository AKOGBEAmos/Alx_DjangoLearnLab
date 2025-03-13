from django.urls import path, include
from .views import list_books, LibraryDetailView, profile, register
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from relationship_app import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', profile, name="profile"),

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Password change views
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Authentication views
    path('accounts/', include('django.contrib.auth.urls')),

]