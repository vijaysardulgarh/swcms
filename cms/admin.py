from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin

#from .models import User
from .models import School
from .models import Affiliation
from .models import Facility
from .models import Nodal
from .models import Event
from .models import Document
from .models import News
from .models import ExtracurricularActivity
from .models import Committee
from .models import CommitteeMember
from .models import CommitteeMeeting    
from .models import Department
from .models import Stream
from .models import Class
from .models import Section
from .models import Subject
from .models import Staff
from .models import Classroom
from .models import Timetable
from .models import Day
from .models import TimetableSlot
from .models import TimetableEntry
from .models import Student
from .models import Topper
from .models import Book


 
admin.site.site_header="Admin Panel PM SHRI GSSS NAGPUR" 
admin.site.site_title="hi"
admin.site.index_title="welcome"
class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff
        fields=('name',"father_name","mother_name","spouse_name","gender","category","date_of_birth","joining_date","retirement_date","subject","email","phone_number")
class StaffAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display =("name","father_name","mother_name","spouse_name","gender","category","date_of_birth","joining_date","retirement_date","subject","email","phone_number")
    resource_class=StaffResource

#admin.site.register(User)    
admin.site.register(School)
admin.site.register(Affiliation)
admin.site.register(Facility)
admin.site.register(Nodal)
admin.site.register(Event)
admin.site.register(Document)
admin.site.register(News)
admin.site.register(ExtracurricularActivity)
admin.site.register(Committee)
admin.site.register(CommitteeMember)
admin.site.register(CommitteeMeeting)
admin.site.register(Department)
admin.site.register(Stream)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Classroom)
admin.site.register(Timetable)
admin.site.register(Day)
admin.site.register(TimetableSlot)
admin.site.register(TimetableEntry)
admin.site.register(Student)
admin.site.register(Topper)
admin.site.register(Book)



