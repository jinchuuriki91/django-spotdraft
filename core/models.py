from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=80)

    def __str__(self):
        return '<Name: {}>'.format(self.name)

    @property
    def course(self):
        return self.participants_set.all()

    @property
    def course_count(self):
        return len(self.course)


class Course(models.Model):

    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(
        Student,
        through='Subscription',
        through_fields=('course', 'student'))

    def __str__(self):
        return '<Name: {}>'.format(self.name)


class Subscription(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()
