# middleware.py
# this is a code to track unique visitors
from .models import Visitor
from django.utils import timezone
import uuid

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.record_visitor(request, response)
        return response

    def record_visitor(self, request, response):
        cookie_id = request.COOKIES.get('visitor_cookie_id')
        if not cookie_id:
            cookie_id = str(uuid.uuid4())  # Generate a unique UUID
            response.set_cookie('visitor_cookie_id', cookie_id)

        ip_address = request.META.get('REMOTE_ADDR')
        existing_visitor = Visitor.objects.filter(cookie_id=cookie_id).first()

        if not existing_visitor:
            Visitor.objects.create(cookie_id=cookie_id, ip_address=ip_address)


# end this is a code to track unique visitors