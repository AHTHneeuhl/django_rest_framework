from rest_framework import serializers

from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = ['title', 'content', 'price', 'sale_price', 'discount']

    def get_discount(self, obj):
        return obj.get_discount()
