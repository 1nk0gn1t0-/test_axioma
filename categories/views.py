from categories.models import Category
from categories.serializers import (
    CategoryListSerializer, CategoryDetailSerializer)
from rest_framework import viewsets
from rest_framework import mixins

class CategoryViewSet(mixins.CreateModelMixin, 
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):

    def get_queryset(self):
        if hasattr(self, 'action') and self.action == 'list':
            return Category.objects.filter(parent=None)

        return Category.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'retrieve':
            return CategoryDetailSerializer

        return CategoryListSerializer
