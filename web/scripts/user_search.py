from django.contrib.auth.models import User

class UserSearch:

    def user_search(self, query: str):
        users = User.objects.all()
        if query:
            from django.db.models import Q
            q = Q(last_name__icontains=query) | Q(first_name__icontains=query)
            for term in query.split():
                q |= Q(first_name__icontains=term) | Q(last_name__icontains=term)
            users = users.filter(q)

        return users
