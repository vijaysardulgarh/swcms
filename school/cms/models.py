from django.db import models
from django.utils import timezone


#from django.contrib.auth.models import AbstractUser


#class User(AbstractUser):
    #STUDENT = 'student'
   # TEACHER = 'teacher'
   # PARENT = 'parent'
   # ADMINISTRATOR = 'administrator'
   # STAFF = 'staff'
   # GUEST = 'guest'

   # USER_TYPE_CHOICES = [
   #     (STUDENT, 'Student'),
   #     (TEACHER, 'Teacher'),
   #     (PARENT, 'Parent/Guardian'),
   #     (ADMINISTRATOR, 'Administrator'),
   #     (STAFF, 'Staff/Non-Teaching Personnel'),
    #    (GUEST, 'Guest/User with Limited Access'),
   # ]

    #user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    #def __str__(self):
    #    return f"{self.username} - {self.get_user_type_display()}"


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)  # Specify upload directory
    accreditation = models.CharField(max_length=255, blank=True)
    established_date = models.DateField(blank=True)
    principal_name = models.CharField(max_length=255, blank=True)
    mission_statement = models.TextField(blank=True)
    vision_statement = models.TextField(blank=True)
    motto = models.CharField(max_length=255, blank=True)
    # Location using GeoDjango (optional)
    #location = models.PointField(blank=True, null=True)  # Requires GeoDjango installation
    social_media_links = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Affiliation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 

    def __str__(self):
        return self.name     
    
    
class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='facility_images/', blank=True)

    def __str__(self):
        return self.name 


class Nodal(models.Model):
    name = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='nodal')
    role = models.CharField(max_length=100)
    responsibilities = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.staff.name if self.staff else ""
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
              
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True)  # Foreign key to Teacher model (optional)
    category = models.CharField(max_length=50, blank=True)  # News category (e.g., "Academics", "Events")
    image = models.ImageField(upload_to='news/', blank=True) 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-date_published']  # Order by most recent first  


class ExtracurricularActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('Sports', 'Sports'),
        ('Clubs', 'Clubs'),
        ('Arts', 'Arts'),
        ('Academic', 'Academic'),
        ('Community Service', 'Community Service'),
        ('Other', 'Other')
    ])
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='activity_images/', blank=True)
    coordinator = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='coordinated_activities')
    participants = models.ManyToManyField('Student', related_name='participated_activities', blank=True)
    requirements = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    registration_link = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Committee(models.Model):
    name = models.CharField(max_length=100)
    objectives = models.TextField(blank=True)
    chairperson = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='chaired_committees')
    tasks = models.TextField(blank=True)
    documents = models.ManyToManyField('Document', related_name='committee', blank=True)

    def __str__(self):
        return self.name
    
class CommitteeMember(models.Model):
    committee=models.ManyToManyField('Committee',related_name='CommitteeMember', blank=True)
    member = models.ManyToManyField('Staff', related_name='CommitteeMember', blank=True)
    designation = models.CharField(max_length=50)  
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='smc_members/', blank=True)  # Optional image field

    def __str__(self):
        return self.member

    class Meta:
        ordering = ['designation']

class CommitteeMeeting(models.Model):

    meeting_schedule = models.CharField(max_length=100, blank=True)
    agenda = models.TextField(blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Committee Meeting on {self.meeting_schedule} "
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    head_of_department = models.OneToOneField('Staff',  on_delete=models.SET_NULL, null=True,related_name='Department')

    def __str__(self):
        return self.name
    

class Class(models.Model):
    CLASS_CHOICES = [
    ('6', '6th'),
    ('7', '7th'),
    ('8', '8th'),
    ('9', '9th'),
    ('10', '10th'),
    ('11', '11th'),
    ('12', '12th'),
]    
    name = models.CharField(max_length=50, unique=True,choices=CLASS_CHOICES)  # Ensure class name is unique
    school = models.ForeignKey(School, on_delete=models.PROTECT)  # Link to School

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Class'

from django.db import models

class Section(models.Model):
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
        # Add more choices as needed
    ]
    name = models.CharField(max_length=2, choices=SECTION_CHOICES)
    section_class = models.ForeignKey('Class', on_delete=models.PROTECT, related_name='sections')

    def __str__(self):
        return f"{self.section_class.name} ({self.name})"

class Subject(models.Model):
    HINDI = 'Hindi'
    ENGLISH = 'English'
    SOCIAL_STUDIES = 'Social Studies'
    SCIENCE = 'Science'
    MATH = 'Math'
    PUNJABI = 'Punjabi'
    COMPUTER = 'Computer'
    HOME_SCIENCE = 'Home Science'
    PHYSICS = 'Physics'
    CHEMISTRY = 'Chemistry'
    ACCOUNT = 'Account'
    BUSINESS = 'Business'
    POLITICAL_SCIENCE = 'Political Science'
    ECONOMICS = 'Economics'
    GEOGRAPHY = 'Geography'
    PSYCHOLOGY = 'Psychology'
    PHYSICAL_EDUCATION = 'Physical Education'
    MUSIC = 'Music'
    AUTOMOBILE = 'Automobile'
    BEAUTY_WELLNESS = 'Beauty & Wellness'

    SUBJECT_CHOICES = [
        (HINDI, 'Hindi'),
        (ENGLISH, 'English'),
        (SOCIAL_STUDIES, 'Social Studies'),
        (SCIENCE, 'Science'),
        (MATH, 'Math'),
        (PUNJABI, 'Punjabi'),
        (COMPUTER, 'Computer'),
        (HOME_SCIENCE, 'Home Science'),
        (PHYSICS, 'Physics'),
        (CHEMISTRY, 'Chemistry'),
        (ACCOUNT, 'Account'),
        (BUSINESS, 'Business'),
        (POLITICAL_SCIENCE, 'Political Science'),
        (ECONOMICS, 'Economics'),
        (GEOGRAPHY, 'Geography'),
        (PSYCHOLOGY, 'Psychology'),
        (PHYSICAL_EDUCATION, 'Physical Education'),
        (MUSIC, 'Music'),
        (AUTOMOBILE, 'Automobile'),
        (BEAUTY_WELLNESS, 'Beauty & Wellness'),
    ]

    name = models.CharField(max_length=100, choices=SUBJECT_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
  #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  school = models.ForeignKey(School, on_delete=models.PROTECT, related_name='staff')
  name = models.CharField(max_length=50)
  father_name = models.CharField(max_length=255, blank=True)
  mother_name = models.CharField(max_length=255, blank=True)
  spouse_name = models.CharField(max_length=255, blank=True) 
  GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  CATEGORY_CHOICES = (
    ('GEN', 'General'),
    ('SC', 'Scheduled Caste'),
    ('ST', 'Scheduled Tribe'),
    ('OBC', 'Other Backward Class'),
    ('EWS', 'Economically Weaker Section'),
    ('OTHER', 'Other'),
    )
  category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, blank=True)
  date_of_birth = models.DateField(blank=True)
  joining_date = models.DateField(blank=True)
  retirement_date = models.DateField(blank=True)
  
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=15, blank=True)
  subject = models.CharField(max_length=50, blank=True)
  profile_picture = models.ImageField(upload_to='staff_profile/', blank=True)
  STAFF_ROLE_CHOICES = [
    ('teaching', 'Teaching'),
    ('non_teaching', 'Non-Teaching'),
]
  staff_role = models.CharField(max_length=20, choices=STAFF_ROLE_CHOICES)
  
  EMPLOYMENT_TYPE_CHOICES = [
    ('regular', 'Regular'),
    ('ssa', 'SSA'),
    ('guest', 'Guest'),
    ('hkrnl', 'HKRNL'),
    ('other', 'Other'),
]
  employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
  bio = models.TextField(blank=True)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ['employment_type','staff_role']



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
    

class TimetableEntry(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimetableSlot, on_delete=models.CASCADE)
    

    # Optional field for handling absent teachers
    #substitute_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ('section', 'slot')  # Ensure no duplicate entries for section and slot

    def __str__(self):
        return f"{self.section.name} - {self.subject.name} - {self.teacher.name} ({self.slot})"
                        



       
class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()
    courses = models.ManyToManyField(Class, related_name='students', blank=True)
    #extracurricular_activities = models.ManyToManyField(ExtracurricularActivity, related_name='participants', blank=True)

    def __str__(self):
        return self.name


    
class Topper(models.Model):
    AWARD_TYPE = (
        ('Topper', 'Topper'),
        ('Shining Star', 'Shining Star')
    )

    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    obtained_marks = models.FloatField()
    total_marks = models.FloatField()
    exam_date = models.DateField()
    position = models.PositiveIntegerField()
    reason = models.TextField(null=True, blank=True)
    date_awarded = models.DateField(null=True, blank=True)
    award_type = models.CharField(max_length=20, choices=AWARD_TYPE,null=True) 


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()

    def __str__(self):
        return self.title   
          



  


      