from django.shortcuts import render
from . import views
from .models import Staff,Student
# Create your views here.
import itertools




def index (request):
     
    staff_members=Staff.objects.all

    sc_Male_count = Student.objects.filter(category='SC', gender='Male').count()
    sc_Female_count = Student.objects.filter(category='SC', gender='Female').count()
    total_sc_students_count = Student.objects.filter(category='SC').count()

    bca_Male_count = Student.objects.filter(category='BCA', gender='Male').count()
    bca_Female_count = Student.objects.filter(category='BCA', gender='Female').count()
    total_bca_students_count = Student.objects.filter(category='BCA').count()

    bcb_Male_count = Student.objects.filter(category='BCB', gender='Male').count()
    bcb_Female_count = Student.objects.filter(category='BCB', gender='Female').count()
    total_bcb_students_count = Student.objects.filter(category='BCB').count()

    gen_Male_count = Student.objects.filter(category='General', gender='Male').count()
    gen_Female_count = Student.objects.filter(category='General', gender='Female').count()
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
        'sc_Male_count': sc_Male_count,
        'sc_Female_count': sc_Female_count,
        'total_sc_students_count': total_sc_students_count,
        'bca_Male_count': bca_Male_count,
        'bca_Female_count': bca_Female_count,
        'total_bca_students_count': total_bca_students_count,
        'bcb_Male_count': bcb_Male_count,
        'bcb_Female_count': bcb_Female_count,
        'total_bcb_students_count': total_bcb_students_count,
        'gen_Male_count': gen_Male_count,
        'gen_Female_count': gen_Female_count,
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

def student_strength(request):
    # Fetch all distinct class names
    classes = Student.objects.values_list('studentclass', flat=True).distinct()

    # Fetch all distinct sections
    sections = Student.objects.values_list('section', flat=True).distinct()

    # Initialize a dictionary to hold statistics for each class and section combination
    class_section_statistics = {}

    # Iterate over each class and section combination
    for class_name in classes:
        for section in sections:
            # Filter students based on class and section
            students = Student.objects.filter(studentclass=class_name, section=section)

            # Calculate counts for each category and gender
            statistics = {
                'SC': {'Male': 0, 'Female': 0},
                'BC-A': {'Male': 0, 'Female': 0},
                'BC-B': {'Male': 0, 'Female': 0},
                'GEN': {'Male': 0, 'Female': 0},
                'Total': {'Male': 0, 'Female': 0},
                'CWSN': {'Male': 0, 'Female': 0},
                'BPL': {'Male': 0, 'Female': 0}
            }

            # Update counts based on the current student's category and gender
            for student in students:
                category_counts = statistics[student.category]
                category_counts[student.gender] += 1

            # Store statistics for the current class and section combination
            class_section_statistics[(class_name, section)] = statistics

    context = {
        'class_section_statistics': class_section_statistics
    }

    return render(request, 'index.html', context)


def about (request):
    
    return render(request,"about.html",{})


    
    