from django.db import models

# Create your models here.
class JobPosting(models.Model):
    # Includes 'id' field, autoincrements starting at 1
    title: str = models.CharField(max_length=100)
    desc: str = models.TextField()
    company: str = models.CharField(max_length=100)
    salary: int = models.IntegerField()
    is_active: bool = models.BooleanField(default=False)  # Only show active posts

    def __str__(self) -> str:
        return f'{self.id}: {self.title} - {self.company} | Active: {self.is_active}'


'''
Example commands -

JobPosting.objects.all() <- selects all
JobPosting.objects.create() <- create individual
JobPosting.objects.filter() <- filter data from db

job = JobPosting.objects.get(id=1) <- Get first item

job.desc = "" <- update desc
job.save() <- save changes to db

job.delete() <- delete from db
'''