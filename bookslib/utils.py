from .models import User


def user_registered(username):
    try:
        User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False


def user_authenticate(uname, pwd):
    user = User.objects.get(username=uname)
    password = user.password
    if password == pwd:
        return True
    else:
        return False
