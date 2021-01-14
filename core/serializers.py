from rest_framework import serializers
from core.models import Student, Course, Subscription


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("id", "name")


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name")


class StudentSubSerializer(serializers.ModelSerializer):

    student = StudentSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ("student", "date_joined", "feedback")


class CourseSubSerializer(serializers.ModelSerializer):

    course = CourseSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ("course", "date_joined", "feedback")


class StudentCourseSerializer(serializers.ModelSerializer):

    courses = CourseSubSerializer(
        many=True, read_only=True, source="subscription_set")
    courses_count = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ("id", "name", "courses", "courses_count")

    def get_courses_count(self, obj):
        return obj.subscription_set.count()


class CourseStudentSerializer(serializers.ModelSerializer):

    students = StudentSubSerializer(
        many=True, read_only=True, source="subscription_set")
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ("id", "name", "students", "students_count")

    def get_students_count(self, obj):
        return obj.subscription_set.count()
