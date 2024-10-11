from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models.skill_endorsement import Skill
from ..models.skill_endorsement import SkillEndorsement
from django.conf import settings


def endorse_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    # Проверка, чтобы пользователь не мог эндорсить свои навыки
    if request.user != skill.user:
        _, created = SkillEndorsement.objects.get_or_create(skill=skill, endorsed_by=request.user)

        # Если запись была создана, проверяем количество подтверждений
        if created:
            endorsement_count = skill.endorsements.count()

            # Если количество подтверждений превышает порог, верифицируем навык
            if endorsement_count >= settings.SKILL_VERIFICATION_THRESHOLD:
                skill.verified = True
                skill.save()

    return redirect('user_profile', user_id=skill.user.id)