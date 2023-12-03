from django.contrib import admin

from .models import JobPosting


class JobBoardAdmin(admin.ModelAdmin):
    site_header = 'Job Board'
    index_title = 'Welcome back!'


# Register models
admin.site.register(JobPosting, JobBoardAdmin)