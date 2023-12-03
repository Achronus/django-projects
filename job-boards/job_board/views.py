from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import JobPosting

# Create your views here.
def index(request) -> HttpResponse:
    active_postings: list = JobPosting.objects.filter(is_active=True)
    context = {
        'job_postings': active_postings
    }
    return render(request, 'index.html', context)

def job_detail(request, pk: int) -> HttpResponse:
    # pk = primary key
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        'posting': job_posting
    }
    return render(request, 'detail.html', context)
