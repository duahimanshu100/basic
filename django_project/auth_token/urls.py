from django.conf.urls import url
from . import api


urlpatterns = [
    url(r'^(?i)api/Login/', api.UserLogin.as_view()),
    url(r'^(?i)api/SignUp/', api.UserSignUp.as_view()),
]
