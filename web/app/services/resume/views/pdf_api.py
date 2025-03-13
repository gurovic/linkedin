from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.services.resume.pdf_parser import parse_pdf
from app.models import UniversityStudent, University


class PDFUploadView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get("file")
        parsed_data = parse_pdf(uploaded_file)
        
        saved_entries = []
        for entry in parsed_data:
            university_name = entry.get("university")
            start_year = entry.get("start_year")
            end_year = entry.get("end_year")

            if not university_name or not start_year:
                continue 

            university, _ = University.objects.get_or_create(name=university_name)
            university_student = UniversityStudent.objects.create(
                student=request.user,
                university=university,
                start_year=start_year,
                end_year=end_year,
            )

            saved_entries.append({
                "university": university.name,
                "start_year": university_student.start_year,
                "end_year": university_student.end_year,
            })

        return JsonResponse({
            "message": "Файл успешно обработан и университеты сохранены.",
            "saved_universities": saved_entries
        }, status=200)
