from django.shortcuts import render
from ..models.company import Company
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'app/company_list.html', {'companies': companies})