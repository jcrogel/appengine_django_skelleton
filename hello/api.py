from models import Newsletter
from rest_framework import routers, serializers, viewsets

class HelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('email_address', 'date_added')

# ViewSets define the view behavior.
class HelloViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = HelloSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'hello', HelloViewSet)