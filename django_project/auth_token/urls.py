from django.conf.urls import url
import api


urlpatterns = [
    url(r'^(?i)api/Login/', api.UserLogin.as_view()),
]
