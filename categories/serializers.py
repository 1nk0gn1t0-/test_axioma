from rest_framework import serializers
from categories.models import Category
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

    def to_internal_value(self, data):
        serializer = CategoryListSerializer(data=data, context=self.context)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class CategoryListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Category.objects.all())])
    children = RecursiveSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children')

    def create_recursive(self, data):
        children = data.pop('children', None)
        parent = Category.objects.create(**data)
        if children is not None:
            for child in children:
                child['parent'] = parent
                self.create_recursive(child)
        
        return parent

    def create(self, validated_data):
        return self.create_recursive(validated_data)


class CategoryDetailSerializer(serializers.ModelSerializer):
    siblings = serializers.SerializerMethodField()
    parents = serializers.SerializerMethodField()
    children = CategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'siblings', 'children', 'parents')
        read_only_fields = ('siblings', 'children', 'parents')

    def get_siblings(self, obj):
        return CategorySerializer(obj.parent.children.exclude(pk=obj.id), many=True).data

    def get_parents(self, obj):
        parents = []
        while obj.parent is not None:
            parents.append(CategorySerializer(obj.parent).data)
            obj = obj.parent
        return parents
