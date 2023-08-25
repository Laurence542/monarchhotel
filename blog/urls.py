from django.conf.urls.static import static
from django.conf import settings
from . import views
from.views import sign_up
from.views import admin_dashboard
from.views import donate
from .views import delete_information
from.views import delete_signup
from.views import customer_bookings
from.views import admin_panel
from.views import my_service
from.views import manage_myservices
from.views import create_projects,manage_project,ContactUs,contact_views,info_web
from django.urls import path
from .views import PostDeleteView


urlpatterns = [
     # Home page
    path('', views.PostList.as_view(), name='home'),

    # Contact Us
    path('contact_us/', views.ContactUs, name='contact_us'),

    # Information Page
    path('info_web/', views.info_web, name='info_web'),

    # Contact View
    path('contact_view/', views.contact_views, name='contact_view'),

    # Admin Panel
    path('admin_panel/', views.admin_panel, name='admin_panel'),

    # Post Deletion
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Create Projects
    path('create_projects/', views.create_projects, name='create_projects'),

    # Manage Projects
    path('manage_project/', views.manage_project, name='manage_project'),

    # Manage My Services
    path('manage_myservices/', views.manage_myservices, name='manage_myservices'),

    # My Services
    path('my_services/', views.my_service, name='my_services'),

    # Customer Booking
    path('customer_booking/', views.customer_bookings, name='customer_booking'),

    # Donate Page
    path('donate/', views.donate, name='donate'),

    # Visitor Count
    path('visitor_count/', views.visitor_count, name='visitor_count'),

    # Delete Signup
    path('delete_signup/<int:signup_id>/', views.delete_signup, name='delete_signup'),

    # Delete Information
    path('delete_information/<int:information_id>/', views.delete_information, name='delete_information'),

    # Admin Dashboard
    path('admin1/', views.admin_dashboard, name='admin1'),

    # Signup Page
    path('signup/', views.sign_up, name='signup'),

    # Login Page
    path('login/', views.login_page, name='login'),

    # Post Detail
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    # Category Filter
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]

# Serve Media Files during Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
