from django.db import models
from django.contrib.auth.models import User

# code for sign up
class Site_Information(models.Model):
    website_name = models.CharField(max_length=255, blank=True)
    slide_image = models.ImageField(null=True, blank = True,upload_to='picture10')
    slide_words = models.CharField(max_length=255, blank=True)
    about_us_images = models.ImageField(null=True, blank = True,upload_to='picture20')
    about_us_words = models.CharField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
# code for sign up
    
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# for blog 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(null=True, blank = True,upload_to='picture')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# for blog 


# code for sign up

class Signup(models.Model):
    username = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    confirm_password = models.TextField(max_length=50)

    def __str__(self):
        return str(self.email)
# end of sign up

# code for contact us
class Contact_us_info(models.Model):
    contact_namess = models.CharField(max_length=255)
    contact_emails = models.EmailField(max_length=255)
    contact_subjects = models.CharField(max_length=50000)
    contact_messages = models.CharField(max_length=5000)

    def __str__(self):
        return self.contact_namess  

# end of contact us      
    
#  code for services   
class Services(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=300)
    
    def __str__(self):
        return str(self.name) 

# end of Services


    
# codefor booking

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateField(max_length=255)
    time = models.TimeField(max_length=255)

    def __str__(self):
        return str(self.name)
    
#  end of booking code   


# code for unique visitors
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    cookie_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=255, blank=True)  # New field

    def __str__(self):
        return self.ip_address
    

# end of code for visitors    