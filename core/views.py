from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Student, Course, Subscription
from core.serializers import (
        StudentSerializer, CourseSerializer,
        StudentCourseSerializer, CourseStudentSerializer)


@api_view(['POST'])
def subscribe_student_course(request, student_id, course_id):
    result = Subscription.objects.filter(course=course_id, student=student_id)
    if result.exists():
        return Response("Already subscribed", status=status.HTTP_200_OK)
    try:
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
    except Exception:
        return Response(
            "Invalid student or course id",
            status=status.HTTP_400_BAD_REQUEST)
    course.participants.add(student)
    return Response("Subscription created", status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def course_feedback(request, student_id, course_id):
    sub = Subscription.objects.filter(student=student_id, course=course_id)
    if sub.exists() is False:
        return Response("Not subscribed", status=status.HTTP_404_NOT_FOUND)
    sub.update(feedback=request.data["feedback"])
    #  sub[0].feedback = request.data["feedback"]
    #  sub[0].save(["feedback"])
    return Response("Feedback saved", status=status.HTTP_200_OK)


class StudentView(APIView):

    def get(self, request, student_id=None):
        if student_id:
            try:
                student = Student.objects.get(id=student_id)
            except Exception:
                return Response("Invalid", status=status.HTTP_404_NOT_FOUND)
            ser = StudentCourseSerializer(student)
            return Response({
                "data": ser.data
                }, status=status.HTTP_200_OK)
        else:
            students = Student.objects.all()
            ser = StudentCourseSerializer(students, many=True)
            return Response({
                "count": len(ser.data),
                "data": ser.data
                }, status=status.HTTP_200_OK)

    def post(self, request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            new_student = ser.save()
        return Response({
            "data": StudentSerializer(new_student).data
            }, status=status.HTTP_201_CREATED)


class CourseView(APIView):

    def get(self, request, course_id=None):
        if course_id:
            try:
                course = Course.objects.get(id=course_id)
            except Exception:
                return Response("Invalid", status=status.HTTP_404_NOT_FOUND)
            ser = CourseStudentSerializer(course)
            return Response({
                "data": ser.data
                }, status=status.HTTP_200_OK)
        else:
            courses = Course.objects.all()
            ser = CourseStudentSerializer(courses, many=True)
            return Response({
                "count": len(ser.data),
                "data": ser.data
                }, status=status.HTTP_200_OK)

    def post(self, request):
        ser = CourseSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            new_course = ser.save()
        return Response({
            "data": CourseSerializer(new_course).data
            }, status=status.HTTP_201_CREATED)
