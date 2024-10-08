from django.shortcuts import render
from ..models import Topic, Event, Employer, Alumni, Vacancy
from copy import deepcopy


class Recommendation:
    # Initializing these outside of __init__ won't work!
    def __init__(self):
        self.weights = {}
        self.name: str = ""
        self.link: str = ""

    @property
    def weight(self):
        return sum(self.weights.values())


def recommendations(request):
    all_topics = list(Topic.objects.all())
    topic_weights = {}
    for i in all_topics:
        id = i.id
        try:
            topic_weights[id] = int(request.GET.get("t" + str(id), "0"))
        except ValueError:
            topic_weights[id] = 0

    what_to_recommend: list[Recommendation] = []
    # TODO: make this look prettier
    for event in Event.objects.all():
        recommendation = Recommendation()
        topics = event.topics.all()
        for topic in all_topics:
            id = topic.id
            recommendation.weights[id] = topic_weights[id] if topics.filter(
                id=id).exists() else 0
        recommendation.link = "/event/" + str(event.id)
        recommendation.name = event.name
        what_to_recommend.append(deepcopy(recommendation))
    for employer in Employer.objects.all():
        recommendation = Recommendation()
        topics = employer.topics.all()
        for topic in all_topics:
            id = topic.id
            recommendation.weights[id] = topic_weights[id] if topics.filter(
                id=id).exists() else 0
        recommendation.link = "/employer/" + str(employer.id)
        recommendation.name = str(employer.name)
        what_to_recommend.append(deepcopy(recommendation))
    for alumni in Alumni.objects.all():
        recommendation = Recommendation()
        topics = alumni.topics.all()
        for topic in all_topics:
            id = topic.id
            recommendation.weights[id] = topic_weights[id] if topics.filter(
                id=id).exists() else 0
        recommendation.link = "/alumni/" + str(alumni.id)
        recommendation.name = str(alumni.name)
        what_to_recommend.append(deepcopy(recommendation))
    for vacancy in Vacancy.objects.all():
        recommendation = Recommendation()
        topics = vacancy.topics.all()
        for topic in all_topics:
            id = topic.id
            recommendation.weights[id] = topic_weights[id] if topics.filter(
                id=id).exists() else 0
        recommendation.link = "/vacancy/" + str(vacancy.id)
        recommendation.name = str(
            vacancy.employer.name) + " " + str(vacancy.salary_per_month)
        what_to_recommend.append(deepcopy(recommendation))

    what_to_recommend = sorted(
        what_to_recommend, key=lambda x: x.weight, reverse=True)

    context = {
        "recommendations": what_to_recommend
    }
    return render(request, "app/recommendations.html", context)
