


from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from webapp.models import Product, Order, OrderProduct


class OrderProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('id',)


class OrderModelSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=OrderProduct.objects.all(), many=True,)
    # product = ProductModelSerializer
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'user')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['products'] = ProductModelSerializer(instance.products.all(), many=True,).data
    #     return data
















# class ArticleModelsSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer(read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), many=True)
#     # tags = TagSerializer(many=True, read_only=True)
#     tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)





# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50, required=True)
#     content = serializers.CharField(max_length=2000, required=True)
#     author = serializers.PrimaryKeyRelatedField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     # test = serializers.CharField(max_length=30, write_only=True)
#
#     def validate(self, attrs):
#         return super().validate(attrs)
#
#     def validate_title(self, value):
#         return value
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance: Article, validated_data):
#         for field, value in validated_data.items():
#             setattr(instance, field, value)
#         instance.save()
#         return instance



# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ("username", "email", "id")
#         # fields = "__all__"

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ("name", "id")
#
#


#
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data["tags"] = TagSerializer(instance.tags.all(), many=True).data
#         return data
#
#
#
#     class Meta:
#         model = Article
#         fields = "__all__"
#         read_only_fields = ("id", "author", "created_at", "updated_at")
#
#
#     def validate_title(self, value):
#         if len(value) < 5:
#             raise ValidationError("Длина маленькая")
#         return value