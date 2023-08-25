from django.views import generic
from .models import Post
from .models import Signup
from .models import Contact_us_info
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.shortcuts import render
from django.views import View
import re
from .models import Post, Category,Services,Booking,Site_Information
from .models import Visitor

class PostDeleteView(View):
    """
    View to delete a Post instance.
    GET: Displays the delete confirmation page.
    POST: Deletes the Post instance and redirects to post list view.
    """
    template_name = 'delete_post.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, self.template_name, {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')

def contact_views(request):
    """
    View to display all contact information.
    Retrieves and displays all Contact_us_info instances.
    """
    view_all_contact = Contact_us_info.objects.all()
    return render(request, 'admin_panel/contactus_view.html', {'view_all_contact': view_all_contact})

def info_web(request):
    """
    View to manage website information.
    Updates Site_Information instance with new data.
    """
    if request.method == 'POST':
        # ... (existing code for updating site information)
        return render(request, 'admin_panel/site_info.html', {'error_message': 'Information changed successfully'})
    return render(request, 'admin_panel/site_info.html')

def ContactUs(request):
    """
    View to handle contact form submissions.
    Validates input and creates a Contact_us_info instance.
    """
    if request.method == 'POST':
        # ... (existing code for handling contact form submissions)
        return render(request, 'contactus.html', {'error_message': 'Your message has been sent successfully.'})
    return render(request, 'contactus.html')

# Other views...

# Views with Generic List and Detail classes...

def sign_up(request):
    """
    View to handle user sign-up.
    Validates input, creates a Signup instance, and displays messages.
    """
    if request.method == 'POST':
        # ... (existing code for user sign-up)
        return render(request, 'signup.html', {'error_message': 'Your account is created successfully.'})
    return render(request, 'signup.html')

def login_page(request):
    """
    View to handle user login.
    Validates input, authenticates the user, and redirects to admin panel.
    """
    if request.method == 'POST':
        # ... (existing code for user login)
        return redirect('admin_panel')
    return render(request, 'login.html')

# Other views...

# Views with user interfaces (UI)...

# You can continue with similar commenting for the rest of your views