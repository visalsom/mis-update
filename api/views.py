from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import Document, Soldier
from api.serializers import DocumentSerializer, SoldierSerializer

# Create your views here.
class SoldierViewSet(CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Soldier.objects.all()
    serializer_class = SoldierSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        user = request.user
        data = request.data
        (soldier, created) = Soldier.objects.get_or_create(user_id = user.id)
        if request.method == 'GET':
            serializer = SoldierSerializer(soldier)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SoldierSerializer(soldier, data = data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.filter(doc_type='D')
    serializer_class = DocumentSerializer

class AnnouncementViewSet(ModelViewSet):
    queryset = Document.objects.filter(doc_type='A')
    serializer_class = DocumentSerializer
    

