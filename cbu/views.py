from rest_framework import viewsets, response, permissions, status

from .models import CBUData, UserTable
from .serializers import CBUDataSerializer


class SaveCBUDataView(viewsets.ModelViewSet):
    serializer_class = CBUDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        CBUData.objects.all().delete()

        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return CBUData.objects.filter(user_table__user = self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user_table=UserTable.objects.get(user = self.request.user))


