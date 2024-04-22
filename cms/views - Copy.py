from django.shortcuts import render
from . import views
from .models import Staff,Student
# Create your views here.
import itertools

from django.db.models import Count, Q

def student_strength(request):


    Student.objects.filter()
    # Define the desired order for classes

    # Query to get student strength by class, section, gender, and caste category
    # Annotate counts for each category

    studentclass1 = {
        'Sixth': 1,
        'Seventh': 2,
        'Eighth': 3,
        'Nineth': 4,
        'Tenth': 5,
        'Eleventh': 6,    
        'Twelth': 7,
        # Add more classes as needed
    }

    sixth_sc_male = Student.objects.filter(studentclass='Sixth', category='SC', gender='Male').values('studentclass','section').annotate(
        count=Count('srn')
    )

    sixth_sc_female = Student.objects.filter(studentclass='Sixth', category='SC', gender='Female').values('section').annotate(
        count=Count('srn')
    ).order_by('section')

    sixth_bca_male = Student.objects.filter(studentclass='Sixth', category='BC-A', gender='Male').values('studentclass','section').annotate(
        count=Count('srn')
    ).order_by('section')

    sixth_bca_female = Student.objects.filter(studentclass='Sixth', category='BC-A', gender='Female').values('studentclass','section').annotate(
        count=Count('srn')
    ).order_by('section')

    seventh_sc_male = Student.objects.filter(studentclass='seventh', category='SC', gender='Male').values('section').annotate(
        seventh_sc_male_total=Count('srn')
    ).order_by('section')

    seventh_sc_female= Student.objects.filter(studentclass='seventh', category='SC', gender='Female').values('section').annotate(
        seventh_sc_male_total=Count('srn')
    ).order_by('section')

    eighth_sc_male = Student.objects.filter(studentclass='Eighth', category='SC', gender='Male').values('section').annotate(
        eighth_sc_male_total=Count('srn')
    ).order_by('section')

    eighth_sc_female = Student.objects.filter(studentclass='Eighth', category='SC', gender='Female').values('section').annotate(
        eighth_sc_female_total=Count('srn')
    ).order_by('section')

    # Filter queryset for SC category for female students
    sc_female_strength = Student.objects.filter(gender='Female', category='SC').values('studentclass', 'section').annotate(
        sc_female_total=Count('srn')
    ).order_by('studentclass', 'section')

    # Similar approach for other categories like BC-A, BC-B, BPL, and CWSN
    # Filter and annotate counts for BC-A category for male and female students
    bca_male_strength = Student.objects.filter(gender='Male', category='BC-A').values('studentclass', 'section').annotate(
        bca_male_total=Count('srn')
    ).order_by('studentclass', 'section')

    bca_female_strength = Student.objects.filter(gender='Female', category='BC-A').values('studentclass', 'section').annotate(
        bca_female_total=Count('srn')
    ).order_by('studentclass', 'section')

    #student = zip(sixth_sc_male, sixth_sc_female,sixth_bca_male, sixth_bca_female,seventh_sc_male,seventh_sc_female,eighth_sc_male,eighth_sc_female) 

    student = zip(sixth_sc_male, sixth_sc_female,sixth_bca_male, sixth_bca_female)
    student_strength = Student.objects.values('studentclass', 'section', 'gender', 'category').annotate(
        total=Count('srn'),
        #total_bpl=Count('srn', filter=Q(is_bpl=True)),
        #total_cwsn=Count('srn', filter=Q(is_cwsn=True))
    ).order_by('studentclass','section')

    context = {
        #'sixth_sc_male':sixth_sc_male,
        #'sixth_sc_female_strength':sixth_sc_female_strength,
        #'seventh_sc_male_strength':seventh_sc_male_strength,
        #'seventh_sc_female_strength':seventh_sc_female_strength,
        #'eighth_sc_male_strength':eighth_sc_male_strength,
        #'eighth_sc_female_strength':eighth_sc_female_strength,
        #'student': student,
        'student_strength': student_strength
    }
    return render(request, 'student_strength.html', context)


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

def student_strength1(request):
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
                'BC_A': {'Male': 0, 'Female': 0},
                'BC_B': {'Male': 0, 'Female': 0},
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

    return render(request, 'student_strength.html', context)


def about (request):
    
    return render(request,"about.html",{})


    
    