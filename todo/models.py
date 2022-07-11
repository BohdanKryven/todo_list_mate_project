from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=155)
    time_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status"]

    def __str__(self):
        return f"Content: {self.content}, status: {self.status}"
