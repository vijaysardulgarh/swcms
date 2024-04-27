from datetime import timedelta
from random import shuffle

def calculate_duration(start_time, end_time):
    return (end_time - start_time).seconds / 3600  # Convert duration to hours

def generate_timetable(classes, subjects, teachers, time_slots, total_duration):
    timetable = []
    remaining_duration = total_duration
    periods_assigned_per_day = {teacher.id: 0 for teacher in teachers}
    periods_assigned_per_week = {teacher.id: 0 for teacher in teachers}

    # Define time slots for each period
    period_durations = [timedelta(minutes=45)] * 4 + [timedelta(minutes=40)] * 4
    shuffle(period_durations)

    subjects = list(classes)
    subjects = list(subjects)
    teachers = list(teachers)
    time_slots = list(time_slots)
    # Shuffle the classes, subjects, teachers, and time slots to randomize the allocation
    shuffle(classes)
    shuffle(subjects)
    shuffle(teachers)
    shuffle(time_slots)

    # Dedicate the first time slots for morning assembly and recess
    morning_assembly_time_slot = time_slots.first()
    morning_assembly_end_time = morning_assembly_time_slot.start_time + timedelta(minutes=20)

    # Update remaining duration
    remaining_duration -= calculate_duration(morning_assembly_time_slot.start_time, morning_assembly_end_time)

    # Dedicate a time slot for recess
    recess_time_slot = time_slots.exclude(id=morning_assembly_time_slot.id).first()
    recess_start_time = recess_time_slot.start_time
    recess_end_time = recess_start_time + timedelta(minutes=30)

    # Update remaining duration
    remaining_duration -= calculate_duration(recess_start_time, recess_end_time)

    for class_obj in classes:
        # Check if the class is from 6th to 8th grade
        if class_obj.grade in ['6th', '7th', '8th']:
            for subject_obj in class_obj.subjects.all():
                # Determine the number of periods per week for the subject
                if subject_obj.name in ['English', 'Math', 'Science', 'Hindi', 'Social Studies']:
                    periods_per_week = 6
                else:
                    periods_per_week = 5

                # Check if the subject has already reached its maximum periods per week
                if periods_assigned_per_week[teacher_obj.id] < periods_per_week:
                    for duration in period_durations:
                        # Determine eligible teachers for the subject based on the provided rules
                        if subject_obj.name == 'English':
                            eligible_teachers = teachers.filter(name__in=['TGT English', 'TGT Social Studies'])
                        elif subject_obj.name == 'Math':
                            eligible_teachers = teachers.filter(name__in=['TGT Science', 'TGT Math'])
                        elif subject_obj.name == 'Science':
                            eligible_teachers = teachers.filter(name='TGT Science')
                        elif subject_obj.name == 'Hindi':
                            eligible_teachers = teachers.filter(name__in=['TGT Sanskrit', 'TGT Hindi'])
                        elif subject_obj.name == 'Social Studies':
                            eligible_teachers = teachers.filter(name='TGT Social Studies')
                        elif subject_obj.name == 'Sanskrit':
                            eligible_teachers = teachers.filter(name='TGT Sanskrit')
                        elif subject_obj.name == 'Punjabi':
                            eligible_teachers = teachers.filter(name='TGT Punjabi')
                        elif subject_obj.name == 'Urdu':
                            eligible_teachers = teachers.filter(name='TGT Urdu')
                        elif subject_obj.name == 'Drawing':
                            eligible_teachers = teachers.filter(name__in=['TGT Fine Arts', 'Drawing Teacher'])
                        elif subject_obj.name == 'Music':
                            eligible_teachers = teachers.filter(name='TGT Music')
                        elif subject_obj.name == 'Home Science':
                            eligible_teachers = teachers.filter(name='TGT Home Science')
                        elif subject_obj.name == 'Physical Education':
                            eligible_teachers = teachers.filter(name__in=['PTI', 'DPE'])

                        if eligible_teachers.exists():
                            for teacher_obj in eligible_teachers:
                                time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                                    id=recess_time_slot.id).first()  # Exclude morning assembly and recess time slots

                                # Calculate the duration of the class
                                class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)

                                if class_duration <= remaining_duration and periods_assigned_per_day[teacher_obj.id] < 6:
                                    # Ensure maximum periods per day and per week constraints
                                    periods_assigned_per_day[teacher_obj.id] += 1
                                    periods_assigned_per_week[teacher_obj.id] += 1
                                    remaining_duration -= class_duration

                                    # Create a timetable entry
                                    timetable.append({
                                        'class_name': class_obj.name,
                                        'subject': subject_obj.name,
                                        'teacher': teacher_obj.name,
                                        'day': time_slot_obj.day,
                                        'start_time': time_slot_obj.start_time,
                                        'end_time': time_slot_obj.start_time + duration
                                    })

                                    # Remove the assigned teacher and time slot from the available lists
                                    teachers = teachers.exclude(id=teacher_obj.id)
                                    time_slots = time_slots.exclude(id=time_slot_obj.id)

                                    # Check if remaining duration is insufficient for another class
                                    if remaining_duration < class_duration:
                                        break  # Skip to the next day

        # Check if the class is from 9th or 10th grade
        elif class_obj.grade in ['9th', '10th']:
            # Define periods per week for each subject
            english_periods_per_week = 8
            math_periods_per_week = 8
            science_periods_per_week = 6
            hindi_periods_per_week = 6
            sanskrit_periods_per_week = 5
            punjabi_periods_per_week = 5
            urdu_periods_per_week = 5
            drawing_periods_per_week = 5
            music_periods_per_week = 5
            home_science_periods_per_week = 5
            physical_education_periods_per_week = 5
            information_technology_periods_per_week = 6
            library_periods_per_week = 4
            
            # Assign periods for each subject
            english_periods_assigned = 0
            math_periods_assigned = 0
            science_periods_assigned = 0
            hindi_periods_assigned = 0
            sanskrit_periods_assigned = 0
            punjabi_periods_assigned = 0
            urdu_periods_assigned = 0
            drawing_periods_assigned = 0
            music_periods_assigned = 0
            home_science_periods_assigned = 0
            physical_education_periods_assigned = 0
            information_technology_periods_assigned = 0
            library_periods_assigned = 0

            # Assign English periods
            english_teacher = teachers.filter(name='PGT English').first()
            for i in range(english_periods_per_week):
                if english_periods_assigned < english_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[english_teacher.id] < 6:
                        periods_assigned_per_day[english_teacher.id] += 1
                        periods_assigned_per_week[english_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'English',
                            'teacher': english_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        english_periods_assigned += 1
                        teachers = teachers.exclude(id=english_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Math periods
            math_teacher = teachers.filter(name='PGT Math').first()
            for i in range(math_periods_per_week):
                if math_periods_assigned < math_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[math_teacher.id] < 6:
                        periods_assigned_per_day[math_teacher.id] += 1
                        periods_assigned_per_week[math_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Math',
                            'teacher': math_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        math_periods_assigned += 1
                        teachers = teachers.exclude(id=math_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Science periods
            science_teachers = teachers.filter(name__in=['PGT Physics', 'PGT Chemistry', 'PGT Biology'])
            for i in range(science_periods_per_week):
                for science_teacher in science_teachers:
                    if science_periods_assigned < science_periods_per_week:
                        time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                            id=recess_time_slot.id).first()
                        class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                        if class_duration <= remaining_duration and periods_assigned_per_day[science_teacher.id] < 6:
                            periods_assigned_per_day[science_teacher.id] += 1
                            periods_assigned_per_week[science_teacher.id] += 1
                            remaining_duration -= class_duration
                            timetable.append({
                                'class_name': class_obj.name,
                                'subject': 'Science',
                                'teacher': science_teacher.name,
                                'day': time_slot_obj.day,
                                'start_time': time_slot_obj.start_time,
                                'end_time': time_slot_obj.start_time + duration
                            })
                            science_periods_assigned += 1
                            teachers = teachers.exclude(id=science_teacher.id)
                            time_slots = time_slots.exclude(id=time_slot_obj.id)
                        if remaining_duration < class_duration:
                            break

            # Assign Hindi periods
            hindi_teachers = teachers.filter(name__in=['PGT Hindi', 'PGT Sanskrit'])
            for i in range(hindi_periods_per_week):
                for hindi_teacher in hindi_teachers:
                    if hindi_periods_assigned < hindi_periods_per_week:
                        time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                            id=recess_time_slot.id).first()
                        class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                        if class_duration <= remaining_duration and periods_assigned_per_day[hindi_teacher.id] < 6:
                            periods_assigned_per_day[hindi_teacher.id] += 1
                            periods_assigned_per_week[hindi_teacher.id] += 1
                            remaining_duration -= class_duration
                            timetable.append({
                                'class_name': class_obj.name,
                                'subject': 'Hindi',
                                'teacher': hindi_teacher.name,
                                'day': time_slot_obj.day,
                                'start_time': time_slot_obj.start_time,
                                'end_time': time_slot_obj.start_time + duration
                            })
                            hindi_periods_assigned += 1
                            teachers = teachers.exclude(id=hindi_teacher.id)
                            time_slots = time_slots.exclude(id=time_slot_obj.id)
                        if remaining_duration < class_duration:
                            break

            # Assign Sanskrit periods
            sanskrit_teacher = teachers.filter(name='PGT Sanskrit').first()
            for i in range(sanskrit_periods_per_week):
                if sanskrit_periods_assigned < sanskrit_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[sanskrit_teacher.id] < 6:
                        periods_assigned_per_day[sanskrit_teacher.id] += 1
                        periods_assigned_per_week[sanskrit_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Sanskrit',
                            'teacher': sanskrit_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        sanskrit_periods_assigned += 1
                        teachers = teachers.exclude(id=sanskrit_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Punjabi periods
            punjabi_teacher = teachers.filter(name='PGT Punjabi').first()
            for i in range(punjabi_periods_per_week):
                if punjabi_periods_assigned < punjabi_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[punjabi_teacher.id] < 6:
                        periods_assigned_per_day[punjabi_teacher.id] += 1
                        periods_assigned_per_week[punjabi_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Punjabi',
                            'teacher': punjabi_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        punjabi_periods_assigned += 1
                        teachers = teachers.exclude(id=punjabi_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Urdu periods
            urdu_teacher = teachers.filter(name='PGT Urdu').first()
            for i in range(urdu_periods_per_week):
                if urdu_periods_assigned < urdu_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[urdu_teacher.id] < 6:
                        periods_assigned_per_day[urdu_teacher.id] += 1
                        periods_assigned_per_week[urdu_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Urdu',
                            'teacher': urdu_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        urdu_periods_assigned += 1
                        teachers = teachers.exclude(id=urdu_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Drawing periods
            drawing_teacher = teachers.filter(name__in=['PGT Fine Arts', 'Drawing Teacher']).first()
            for i in range(drawing_periods_per_week):
                if drawing_periods_assigned < drawing_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[drawing_teacher.id] < 6:
                        periods_assigned_per_day[drawing_teacher.id] += 1
                        periods_assigned_per_week[drawing_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Drawing',
                            'teacher': drawing_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        drawing_periods_assigned += 1
                        teachers = teachers.exclude(id=drawing_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Music periods
            music_teacher = teachers.filter(name='PGT Music').first()
            for i in range(music_periods_per_week):
                if music_periods_assigned < music_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[music_teacher.id] < 6:
                        periods_assigned_per_day[music_teacher.id] += 1
                        periods_assigned_per_week[music_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Music',
                            'teacher': music_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        music_periods_assigned += 1
                        teachers = teachers.exclude(id=music_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Home Science periods
            home_science_teacher = teachers.filter(name='PGT Home Science').first()
            for i in range(home_science_periods_per_week):
                if home_science_periods_assigned < home_science_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[home_science_teacher.id] < 6:
                        periods_assigned_per_day[home_science_teacher.id] += 1
                        periods_assigned_per_week[home_science_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Home Science',
                            'teacher': home_science_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        home_science_periods_assigned += 1
                        teachers = teachers.exclude(id=home_science_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Physical Education periods
            physical_education_teachers = teachers.filter(name__in=['PTI', 'DPE'])
            for i in range(physical_education_periods_per_week):
                for physical_education_teacher in physical_education_teachers:
                    if physical_education_periods_assigned < physical_education_periods_per_week:
                        time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                            id=recess_time_slot.id).first()
                        class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                        if class_duration <= remaining_duration and periods_assigned_per_day[physical_education_teacher.id] < 6:
                            periods_assigned_per_day[physical_education_teacher.id] += 1
                            periods_assigned_per_week[physical_education_teacher.id] += 1
                            remaining_duration -= class_duration
                            timetable.append({
                                'class_name': class_obj.name,
                                'subject': 'Physical Education',
                                'teacher': physical_education_teacher.name,
                                'day': time_slot_obj.day,
                                'start_time': time_slot_obj.start_time,
                                'end_time': time_slot_obj.start_time + duration
                            })
                            physical_education_periods_assigned += 1
                            teachers = teachers.exclude(id=physical_education_teacher.id)
                            time_slots = time_slots.exclude(id=time_slot_obj.id)
                        if remaining_duration < class_duration:
                            break

            # Assign Information Technology periods
            information_technology_teacher = teachers.filter(name__in=['PGT Computer Science', 'Computer Teacher']).first()
            for i in range(information_technology_periods_per_week):
                if information_technology_periods_assigned < information_technology_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[information_technology_teacher.id] < 6:
                        periods_assigned_per_day[information_technology_teacher.id] += 1
                        periods_assigned_per_week[information_technology_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Information Technology',
                            'teacher': information_technology_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        information_technology_periods_assigned += 1
                        teachers = teachers.exclude(id=information_technology_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

            # Assign Library periods
            library_periods_assigned = 0
            library_teacher = teachers.filter(name__in=['Librarian', 'Library Teacher']).first()
            for i in range(library_periods_per_week):
                if library_periods_assigned < library_periods_per_week:
                    time_slot_obj = time_slots.exclude(id=morning_assembly_time_slot.id).exclude(
                        id=recess_time_slot.id).first()
                    class_duration = calculate_duration(time_slot_obj.start_time, time_slot_obj.start_time + duration)
                    if class_duration <= remaining_duration and periods_assigned_per_day[library_teacher.id] < 6:
                        periods_assigned_per_day[library_teacher.id] += 1
                        periods_assigned_per_week[library_teacher.id] += 1
                        remaining_duration -= class_duration
                        timetable.append({
                            'class_name': class_obj.name,
                            'subject': 'Library',
                            'teacher': library_teacher.name,
                            'day': time_slot_obj.day,
                            'start_time': time_slot_obj.start_time,
                            'end_time': time_slot_obj.start_time + duration
                        })
                        library_periods_assigned += 1
                        teachers = teachers.exclude(id=library_teacher.id)
                        time_slots = time_slots.exclude(id=time_slot_obj.id)
                    if remaining_duration < class_duration:
                        break

    return timetable
