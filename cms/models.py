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
    established_date = models.DateField(null=True, blank=True)
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

    class Meta:
        verbose_name_plural = 'Facilities'

class Nodal(models.Model):
    name = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='nodal')
    role = models.CharField(max_length=100)
    responsibilities = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.name.name if self.name else ""
    

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
    
    class Meta:
        verbose_name_plural = 'Extracurricular Activities'
        
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
    
class Stream(models.Model):
    SCIENCE = 'Science'
    COMMERCE = 'Commerce'
    ARTS = 'Arts'

    STREAM_CHOICES = [
        (SCIENCE, 'Science'),
        (COMMERCE, 'Commerce'),
        (ARTS, 'Arts'),
        # Add more streams as needed
    ]

    name = models.CharField(max_length=100, choices=STREAM_CHOICES, unique=True)
    

    def __str__(self):
        return self.name
    
class Class(models.Model):
    CLASS_CHOICES = [
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
    ('na', 'NA'),
]    
    name = models.CharField(max_length=50, unique=True,choices=CLASS_CHOICES)  # Ensure class name is unique
    school = models.ForeignKey(School, on_delete=models.PROTECT)  # Link to School

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Class'



class Stream(models.Model):
    SCIENCE = 'Science'
    COMMERCE = 'Commerce'
    ARTS = 'Arts'

    STREAM_CHOICES = [
        (SCIENCE, 'Science'),
        (COMMERCE, 'Commerce'),
        (ARTS, 'Arts'),
        # Add more streams as needed
    ]

    name = models.CharField(max_length=100, choices=STREAM_CHOICES)

    def __str__(self):
        return self.get_name_display()


class Section(models.Model):
    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('na', 'NA'),
        # Add more choices as needed
    ]
    name = models.CharField(max_length=2, choices=SECTION_CHOICES)
    section_class = models.ForeignKey('Class', on_delete=models.PROTECT, related_name='sections')
    section_stream = models.ForeignKey('Stream', on_delete=models.PROTECT, related_name='sections')
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
  employee_id = models.CharField(max_length=20, unique=True)
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
  date_of_birth = models.DateField(null=True, blank=True)
  joining_date = models.DateField(null=True, blank=True)
  retirement_date = models.DateField(null=True, blank=True)
  
  email = models.EmailField(unique=True, blank=True)
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
    ('nsqf', 'NSQF'),
    ('other', 'Other'),
]
  employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
  bio = models.TextField(blank=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Staff'
    ordering = ['employment_type','staff_role']

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ClassIncharge(models.Model):
    name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    class_alloted = models.ForeignKey(Class, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.teacher.name} - {self.classroom.name} - {self.class_alloted} - {self.section}"
    
class Timetable(models.Model):


    SEASON_CHOICES = (
        ('winter', 'winter'),
        ('summer', 'Summer'),
        ('other', 'Other'),
        # Add more semesters as needed
    )

    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        # Add more days as needed
    )

    CLASS_TYPE_CHOICES = (
        ('Regular', 'Regular'),
        ('Assembly', 'Assembly'),
        ('Recess', 'Recess'),
        ('Special', 'Special Event'),
        # Add more types as needed
    )

    
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    class_name = models.ForeignKey('Class', on_delete=models.PROTECT, related_name='Timetable')
    section = models.ForeignKey('Section', on_delete=models.PROTECT, related_name='timetable')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=10, choices=CLASS_TYPE_CHOICES, default='Regular')
    teachers = models.ManyToManyField(Staff, blank=True)
    classrooms = models.ManyToManyField(Classroom, blank=True)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_mandatory = models.BooleanField(default=True)
 

    def __str__(self):
        return f"{self.day}, {self.start_time} - {self.end_time}: {self.class_name} ({self.section})"


class Day(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    name = models.CharField(max_length=20, choices=DAY_CHOICES)

    def __str__(self):
        return self.name


class TimetableSlot(models.Model):

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day.name} - {self.start_time} - {self.end_time}"

class TimetableEntry(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimetableSlot, on_delete=models.CASCADE)
    

    # Optional field for handling absent teachers
    #substitute_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Time Table Entries'
        unique_together = ('section', 'slot')  # Ensure no duplicate entries for section and slot

    def __str__(self):
        return f"{self.section.name} - {self.subject.name} - {self.teacher.name} ({self.slot})"
                        



class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sr_no = models.CharField(max_length=20)
    srn = models.CharField(max_length=20)
    school_code = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    admission_date = models.DateField()
    class_field = models.CharField(max_length=20)
    stream = models.CharField(max_length=20,blank=True, null=True)
    section = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=20)
    admission_number = models.CharField(max_length=20)
    title = models.CharField(max_length=10, blank=True, null=True)
    full_name_aadhar = models.CharField(max_length=255)
    name_in_local_language = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    eid_number = models.CharField(max_length=20, blank=True, null=True)
    domicile_of_haryana = models.BooleanField(default=False)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    birth_country = models.CharField(max_length=255, blank=True, null=True)
    birth_state = models.CharField(max_length=255, blank=True, null=True)
    birth_district = models.CharField(max_length=255, blank=True, null=True)
    birth_sub_district = models.CharField(max_length=100, blank=True, null=True)
    birth_city_village_town = models.CharField(max_length=255, blank=True, null=True)
    is_father_alive = models.BooleanField(default=True)
    father_title = models.CharField(max_length=10, blank=True, null=True)
    father_full_name_aadhar = models.CharField(max_length=255)
    father_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    is_father_unclean_occupation = models.BooleanField(default=False)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_highest_qualification = models.CharField(max_length=100, blank=True, null=True)
    father_pan = models.CharField(max_length=20, blank=True, null=True)
    is_father_income_tax_payer = models.BooleanField(default=False)
    is_mother_alive = models.BooleanField(default=True)
    mother_title = models.CharField(max_length=10, blank=True, null=True)
    mother_full_name_aadhar = models.CharField(max_length=255)
    mother_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    is_mother_unclean_occupation = models.BooleanField(default=False)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_highest_qualification = models.CharField(max_length=100, blank=True, null=True)
    mother_pan = models.CharField(max_length=20, blank=True, null=True)
    is_mother_tax_payer = models.BooleanField(default=False,)
    guardian_title = models.CharField(max_length=10, blank=True, null=True)
    guardian_full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    guardian_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    guardian_occupation = models.CharField(max_length=100, blank=True, null=True)
    family_annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bpl_certificate_number = models.CharField(max_length=20, blank=True, null=True)
    bpl_certificate_issuing_authority = models.CharField(max_length=255, blank=True, null=True)
    bpl_certificate_issued_date = models.DateField(blank=True, null=True)
    sibling_srn = models.CharField(max_length=20, blank=True, null=True)
    sibling_legal_full_name = models.CharField(max_length=255, blank=True, null=True)
    sibling_date_of_birth = models.DateField(blank=True, null=True)
    sibling_class = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    sub_district = models.CharField(max_length=100, blank=True, null=True)
    city_village_town = models.CharField(max_length=100, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    address_line3 = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    father_email = models.EmailField(blank=True, null=True)
    father_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    mother_email = models.EmailField(blank=True, null=True)
    mother_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    guardian_email = models.EmailField(blank=True, null=True)
    guardian_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    name_on_passbook = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    account_type = models.CharField(max_length=20, blank=True, null=True)
    account_status = models.CharField(max_length=20, blank=True, null=True)
    joint_account_holder_name = models.CharField(max_length=255, blank=True, null=True)
    joint_account_holder_relation = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)
    micr_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    subjects_opted_by_student = models.CharField(max_length=255, blank=True, null=True)
    caste_name = models.CharField(max_length=100, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    religion_name = models.CharField(max_length=100, blank=True, null=True)
    caste_certificate_number = models.CharField(max_length=20, blank=True, null=True)
    caste_certificate_issuing_authority = models.CharField(max_length=255, blank=True, null=True)
    caste_certificate_issued_date = models.DateField(blank=True, null=True)
    disability = models.BooleanField(default=False, blank=True, null=True)
    disorder_name = models.CharField(max_length=100, blank=True, null=True)

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
          



  


      