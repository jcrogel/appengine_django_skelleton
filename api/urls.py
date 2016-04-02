from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework import serializers, viewsets

import accounts.api
import hello.api

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(accounts.api.router.urls)),
    url(r'^', include(hello.api.router.urls)),
]