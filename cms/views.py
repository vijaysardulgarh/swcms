from django.shortcuts import render
from . import views
from .models import Staff,Student
# Create your views here.
def index (request):
     
    staff_members=Staff.objects.all

    sc_boys_count = Student.objects.filter(category='SC', gender='Male').count()
    sc_girls_count = Student.objects.filter(category='SC', gender='Female').count()
    total_sc_students_count = Student.objects.filter(category='SC').count()

    bca_boys_count = Student.objects.filter(category='BCA', gender='Male').count()
    bca_girls_count = Student.objects.filter(category='BCA', gender='Female').count()
    total_bca_students_count = Student.objects.filter(category='BCA').count()

    bcb_boys_count = Student.objects.filter(category='BCB', gender='Male').count()
    bcb_girls_count = Student.objects.filter(category='BCB', gender='Female').count()
    total_bcb_students_count = Student.objects.filter(category='BCB').count()

    gen_boys_count = Student.objects.filter(category='General', gender='Male').count()
    gen_girls_count = Student.objects.filter(category='General', gender='Female').count()
    total_gen_students_count = Student.objects.filter(category='General').count()

    sc_male_teachers_count = Staff.objects.filter(category='SC', gender='Male').count()
    sc_female_teachers_count = Staff.objects.filter(category='SC', gender='Female').count()
    total_sc_teachers_count = Staff.objects.filter(category='SC').count()

    bca_male_teachers_count = Staff.objects.filter(category='BC-A', gender='Male').count()
    bca_female_teachers_count = Staff.objects.filter(category='BC-A', gender='Female').count()
    total_bca_teachers_count = Staff.objects.filter(category='BC-A').count()

    bcb_male_teachers_count = Staff.objects.filter(category='BC-B', gender='Male').count()
    bcb_female_teachers_count = Staff.objects.filter(category='BC-B', gender='Female').count()
    total_bcb_teachers_count = Staff.objects.filter(category='BC-B').count()

    gen_male_teachers_count = Staff.objects.filter(category='GEN', gender='Male').count()
    gen_female_teachers_count = Staff.objects.filter(category='GEN', gender='Female').count()
    total_gen_teachers_count = Staff.objects.filter(category='GEN').count()

    context = {
        'staff_members':staff_members,
        'sc_boys_count': sc_boys_count,
        'sc_girls_count': sc_girls_count,
        'total_sc_students_count': total_sc_students_count,
        'bca_boys_count': bca_boys_count,
        'bca_girls_count': bca_girls_count,
        'total_bca_students_count': total_bca_students_count,
        'bcb_boys_count': bcb_boys_count,
        'bcb_girls_count': bcb_girls_count,
        'total_bcb_students_count': total_bcb_students_count,
        'gen_boys_count': gen_boys_count,
        'gen_girls_count': gen_girls_count,
        'total_gen_students_count': total_gen_students_count,
        'sc_male_teachers_count': sc_male_teachers_count,
        'sc_female_teachers_count': sc_female_teachers_count,
        'total_sc_teachers_count': total_sc_teachers_count,
        'bca_male_teachers_count': bca_male_teachers_count,
        'bca_female_teachers_count': bca_female_teachers_count,
        'total_bca_teachers_count': total_bca_teachers_count,
        'bcb_male_teachers_count': bcb_male_teachers_count,
        'bcb_female_teachers_count': bcb_female_teachers_count,
        'total_bcb_teachers_count': total_bcb_teachers_count,
        'gen_male_teachers_count': gen_male_teachers_count,
        'gen_female_teachers_count': gen_female_teachers_count,
        'total_gen_teachers_count': total_gen_teachers_count,
    }



    return render(request, 'index.html', context)
   
 

def about (request):
    
    return render(request,"about.html",{})


    
    