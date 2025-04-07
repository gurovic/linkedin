from django.contrib.auth.models import User

class UserSearch:

    def user_search(self, query: str):
        users = User.objects.all()
        if query:
            users = users.filter(
                last_name__icontains=query,
            ) | users.filter(
                first_name__icontains=query,
            ) | users.filter(
                first_name__icontains=query.split(" ")[0],
            ) | users.filter(
                last_name__icontains=query.split(" ")[0],
            ) | users.filter(
                first_name__icontains=query.split(" ")[-1],
            ) | users.filter(
                last_name__icontains=query.split(" ")[-1],
            )
        return users
