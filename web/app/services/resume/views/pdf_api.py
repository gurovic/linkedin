from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.models import University, UniversityStudent
from app.models.job_experience import JobExperience
from app.models.skill import Skill, UserSkill
from app.services.resume.pdf_parser import parse_pdf
from app.services.resume.resume_analyzer import analyze_resume


@method_decorator(csrf_exempt, name="dispatch")
class PDFUploadView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get("file")
        parsed_text = parse_pdf(uploaded_file)

        analysis_result = analyze_resume(parsed_text)

        if "error" in analysis_result:
            return JsonResponse(
                {"error": analysis_result["error"]},
                status=500,
            )

        saved_universities = []
        saved_jobs = []
        saved_skills = []

        # --- Университеты ---
        for edu in analysis_result.get("education", []):
            university_name = edu.get("university")
            start_year = edu.get("start_year")
            end_year = edu.get("end_year")

            if not university_name or not start_year:
                continue

            if UniversityStudent.objects.filter(
                university__name=university_name,
                student=request.user,
                start_year=start_year,
            ):
                continue

            university, _ = University.objects.get_or_create(
                name=university_name,
            )
            university_student = UniversityStudent.objects.create(
                student=request.user,
                university=university,
                start_year=start_year,
                end_year=end_year,
            )

            saved_universities.append(
                {
                    "university": university.name,
                    "start_year": start_year,
                    "end_year": end_year,
                },
            )

        # --- Опыт работы ---
        for job in analysis_result.get("work_experience", []):
            company_name = job.get("company")
            position = job.get("position")
            start_year = job.get("start_year")
            end_year = job.get("end_year")

            if not company_name or not position or not start_year or not end_year:
                continue

            if JobExperience.objects.filter(
                company_name=company_name,
                position=position,
                start_year=start_year,
                user=request.user,
            ):
                continue

            JobExperience.objects.create(
                user=request.user,
                company_name=company_name,
                position=position,
                start_year=start_year,
                end_year=end_year,
            )

            saved_jobs.append(
                {
                    "company_name": company_name,
                    "position": position,
                    "start_year": start_year,
                    "end_year": end_year,
                },
            )

        # --- Навыки ---
        for skill_name in analysis_result.get("skills", []):
            if not skill_name:
                continue
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name.strip())
            UserSkill.objects.get_or_create(user=request.user, skill=skill_obj)
            saved_skills.append(skill_obj.name)

        return JsonResponse(
            {
                "message": "Файл успешно обработан и данные сохранены.",
                "saved_universities": saved_universities,
                "saved_work_experience": saved_jobs,
                "saved_skills": saved_skills,
            },
            status=200,
            json_dumps_params={"ensure_ascii": False},
            content_type="application/json; charset=utf-8",
        )
