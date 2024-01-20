from bbtest.models import User
from pprint import pprint

us = User.objects.all()

us[0].user_permissions.all()

res = []
for u in us:
    res.append([u.username, u.user_permissions.all()])

pprint(res)

User.objects.filter(user_permissions__codename="expert").all()

User.active_users.filter(user_permissions__codename="student").count()
User.objects.filter(user_permissions__codename="developer").count()
User.active_users.filter(user_permissions__codename="admin").count()
User.active_users.filter(user_permissions__codename="expert").count()
User.active_users.filter(is_superuser=True).count()


res = []
for u in us:
    if u.is_superuser:
        res.append("super: {}".format(str(u.username)) )
        continue
    codename = str(u.user_permissions.get().codename)
    if codename == "student":
        continue
    res.append("{}: {}".format(codename, str(u.username)) )

pprint(res)

    # res.append([u.username, u.user_permissions.all()])


User.objects.get(username="Dev-007")

from bbtest.models import User
user = User.objects.get(username="Expert-007")
user.expert_profile