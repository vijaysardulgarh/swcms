# swcms
School Website Content Management System
Author -Vijay Kumar

Create a Folder swcms

create Virtual Enviornment

    python -m venv venv

Activate virtual Enviornment
    
    source venv/Scripts/activate

Install Django

    pip install django
    

Create Django Project in Present Working Directory

    django-admin startproject school .
    

Test Server

    python manage.py runserver 


Apply Admin Migrations

    python manage.py migrate

Create Admin Login

    python manage.py createsuperuser

Create a django app

    python manage.py startapp cms

Now open the setting.py file in your project folder and add cms app to installed app section

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    ]


Create a new file in cms folder and save it with name urls.py 

    from django.urls import path

    urlpatterns = [
    path('',views.index,name='index'),
    ]

Now route this file in urls.py file in school folder

    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include("cms.urls")),
    ]

 now Create a view for this. Goto view file in cms folder

    from django.shortcuts import render
    from . import views

    def index (request):
    return render(request,"index.html",{})

Create a templates folder in cms app and create html files index.html

index.html

    <!DOCTYPE html>
    
        <head>

        </head>
        
        <body>
   
        Hello! I am Home Page
        
        </body>
        
    </html>

Install Package pillow for image field

    python -m pip install pillow
    
Add following model code to model file in cms folder

    from django.db import models
    from django.utils import timezone
    
    class School(models.Model):
        name = models.CharField(max_length=255)
        address = models.TextField(blank=True)
        website = models.URLField(blank=True)
        email = models.EmailField(blank=True)
        phone_number = models.CharField(max_length=15, blank=True)
        logo = models.ImageField(upload_to='logos/', blank=True)  # Specify upload directory
        motto = models.CharField(max_length=255, blank=True)
        established_date = models.DateField(blank=True)
        principal_name = models.CharField(max_length=255, blank=True)
        description = models.TextField(blank=True)
    
        # Location using GeoDjango (optional)
        #location = models.PointField(blank=True, null=True)  # Requires GeoDjango installation
    
        def __str__(self):
            return self.name
    
    class Class(models.Model):
        name = models.CharField(max_length=50, unique=True)  # Ensure class name is unique
        school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    
        def __str__(self):
            return self.name
        class Meta:
            verbose_name_plural = 'Class'
            
    class Section(models.Model):
        name = models.CharField(max_length=50)
        class_level = models.ForeignKey(Class, on_delete=models.CASCADE)  # Link to Class
    
        def __str__(self):
            return f"{self.class_level.name} - {self.name}"
    
    class Subject(models.Model):
        name = models.CharField(max_length=100, unique=True)  # Ensure subject name is unique
    
        def __str__(self):
            return self.name
        
    class TimetableSlot(models.Model):
        day = models.CharField(max_length=10, choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
        ])
        start_time = models.TimeField()
        end_time = models.TimeField()
    
        def __str__(self):
            return f"{self.day} - {self.start_time} - {self.end_time}"
    
    class Teacher(models.Model):
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email = models.EmailField(unique=True)
      phone_number = models.CharField(max_length=15, blank=True)
      subject = models.CharField(max_length=50, blank=True)
      bio = models.TextField(blank=True)
      image = models.ImageField(upload_to='teachers/', blank=True)
      date_of_birth = models.DateField(blank=True, null=True)
      joining_date = models.DateField(blank=True, null=True)
      retirement_date = models.DateField(blank=True, null=True)
      GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )
      gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
      CATEGORY_CHOICES = (
            ('GEN', 'General'),
            ('SC', 'Scheduled Caste'),
            ('ST', 'Scheduled Tribe'),
            ('OBC', 'Other Backward Class'),
            ('EWS', 'Economically Weaker Section'),
            ('OTHER', 'Other'),
        )
      category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, blank=True)
      father_name = models.CharField(max_length=255, blank=True)
      mother_name = models.CharField(max_length=255, blank=True)
      spouse_name = models.CharField(max_length=255, blank=True) 
    
      def __str__(self):
        return f"{self.first_name} {self.last_name}"
      
      class Meta:
        ordering = ['first_name','last_name']
    
    class TimetableEntry(models.Model):
        section = models.ForeignKey(Section, on_delete=models.CASCADE)
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        slot = models.ForeignKey(TimetableSlot, on_delete=models.CASCADE)
        school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    
        # Optional field for handling absent teachers
        #substitute_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    
        class Meta:
            unique_together = ('section', 'slot')  # Ensure no duplicate entries for section and slot
    
        def __str__(self):
            return f"{self.section.name} - {self.subject.name} - {self.teacher.name} ({self.slot})"
                            
    
    
    class SmcCommitteeMember(models.Model):
        name = models.CharField(max_length=100)
        designation = models.CharField(max_length=50)  
        email = models.EmailField(blank=True)
        phone_number = models.CharField(max_length=15, blank=True)
        image = models.ImageField(upload_to='smc_members/', blank=True)  # Optional image field
    
        def __str__(self):
            return self.name
    
        class Meta:
            ordering = ['designation', 'name']
    
    class Affiliation(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        website = models.URLField(blank=True)  # Website URL
        logo = models.ImageField(upload_to='affiliations/', blank=True)  
    
        def __str__(self):
            return self.name        
        
    class News(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        date_published = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)  # Foreign key to Teacher model (optional)
        category = models.CharField(max_length=50, blank=True)  # News category (e.g., "Academics", "Events")
        image = models.ImageField(upload_to='news/', blank=True) 
        def __str__(self):
            return self.title
    
        class Meta:
            verbose_name_plural = 'News'
            ordering = ['-date_published']  # Order by most recent first    
