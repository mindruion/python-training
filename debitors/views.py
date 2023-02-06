from rest_framework.response import Response
from rest_framework.views import APIView

from debitors.models import Debitor
from debitors.serializers import DebitorSerializer


class DebitorViews(APIView):
    def get(self, request):
        debitors = Debitor.objects.all()
        serializer = DebitorSerializer(debitors, many=True)
        return Response(dict(debitors=serializer.data))

