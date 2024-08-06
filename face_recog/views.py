from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Student

import numpy as np

from .utils import get_face_encoding
from .forms import StudentForm

def index(request):
    return render(request, 'student.html')

def detect_face(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
            face_encoding = get_face_encoding(image)

            if face_encoding is not None:
                students = Student.objects.all()
                min_dist = float('inf')
                identified_student = None

                for student in students:
                    for db_face_encoding in student.face_encodings:
                        dist = np.linalg.norm(face_encoding - np.array(db_face_encoding))
                        print(f"Distance for {student.name}: {dist}")
                        if dist < min_dist:
                            min_dist = dist
                            identified_student = student
                
                if identified_student and min_dist < 0.6:  # Threshold value for face matching
                    return JsonResponse({
                        'name': identified_student.name, 
                        'registration_id': identified_student.registration_id, 
                        'branch': identified_student.branch
                    })
                
                return JsonResponse({'error': 'No match found'})
            else:
                return JsonResponse({'error': 'No face detected in the image'})

    return JsonResponse({'error': 'Invalid request method'})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            face_encodings = []

            for image in request.FILES.getlist('images'):
                encoding = get_face_encoding(image)
                if encoding is not None:
                    face_encodings.append(encoding.tolist())
            
            if face_encodings:
                student.face_encodings = face_encodings
                student.save()
                return redirect('index')
            else:
                form.add_error('images', 'No valid faces detected in any images.')

        else:
            print("Form is not valid")
            print(form.errors)

    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})

