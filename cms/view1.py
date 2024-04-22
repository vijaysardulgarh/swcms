from django.shortcuts import render

from .models import Student

def student_strength(request):
  # Optionally filter by class and section
  students = Student.objects.all()  # Get all students

  # Build table data dictionary
  table_data = {}
  for student in students:
    class_section = (student.studentclass, student.section)
    category = table_data.get(class_section, {})  # Get existing data for class/section (or empty dict)
    category.setdefault('Boys', 0)  # Initialize Boy count (if not present)
    category.setdefault('Girls', 0)  # Initialize Girl count (if not present)
    
    # Increment count based on category and gender
    if student.category == 'SC':
      if student.gender == 'Male':
        category['Boys'] += 1
      else:
        category['Girls'] += 1
    # Similar logic for BCA, BCB, and GEN categories
    
    # Calculate total for class/section
    category['BoysTotal'] = sum(category.values()) if category else 0
    category['GirlsTotal'] = sum(category.values()) if category else 0
    
    # Handle CWSN and BPL (assuming boolean fields in the model)
    category['CWSNBoys'] = category.get('Boys', 0) if student.disability else 0
    category['CWSNGirls'] = category.get('Girls', 0) if student.disability else 0
    category['BPLBoys'] = category.get('Boys', 0) if student.category == 'BPL' else 0
    category['BPLGirls'] = category.get('Girls', 0) if student.category == 'BPL' else 0
    
    table_data[class_section] = category  # Update data for class/section

  context = {'table_data': table_data}  # Pass data to template
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

def about (request):
    
    return render(request,"about.html",{})