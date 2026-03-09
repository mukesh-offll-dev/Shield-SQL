from django.db import models

class Participant(models.Model):
    student_name = models.CharField(max_length=100)
    planner_answer = models.CharField(max_length=100)
    completion_time = models.IntegerField()  # in seconds
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.planner_answer} ({self.completion_time}s)"
