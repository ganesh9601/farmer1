from rest_framework.serializers import ModelSerializer
from .models import product,Checkout,Cart,Discount


class productSerializer(ModelSerializer):
    class Meta:
        model=product
        fields="__all__"

class CheckoutSerializer(ModelSerializer):
    class Meta:
        model=Checkout
        fields="__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"

class DiscountSerializer(ModelSerializer):
    class Meta:
        model=Discount
        fields="__all__"

