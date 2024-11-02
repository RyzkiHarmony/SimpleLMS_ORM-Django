from django.shortcuts import render, HttpResponse
from core.models import Course, CourseContent, CourseMember, User, Comment
from django.http.response import  JsonResponse

# Create your views here.
def index(request):
    return  HttpResponse("Hello, world!")

def testing(request):
    guru = User.objects.create_user(
            username = "guru_1", email=  "guru1@gmail.com", password = "guru123",
            first_name = "Guru", last_name = "Satu",
            )

    Course.objects.create(
        name = "Pemrograman Python",
        description = "Pemrograman Python adalah bahasa pemrograman yang populer digunakan",
        price = 50000,
        teacher = guru,

    )
    return HttpResponse("Testing")

def allCourses(request):
    allCourses = Course.objects.all()
    result = []
    for course in allCourses:
        record = {'id': course.id, 'name': course.name, 
                  'price': course.price,
                  'teacher': {
                      'id': course.teacher.id,
                      'username': course.teacher.username,
                      'email': course.teacher.email,
                      'fullname': f"{course.teacher.first_name} {course.teacher.last_name}"
                  }}
        result.append(record)
    return JsonResponse(result, safe=False)

def userCourses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = Course.objects.filter(teacher=user.id)
    course_data = []
    for course in courses:
        record = {'id': course.id, 'name': course.name, 
                  'description': course.description, 'price': course.price}
        course_data.append(record)
    result = {'id': user.id, 'username': user.username, 'email': user.email, 
              'fullname': f"{user.first_name} {user.last_name}", 
              'courses': course_data}
    return JsonResponse(result, safe=False)