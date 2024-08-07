from rest_framework import serializers
from . models import *




class AddressModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ="__all__"



class UserModelSerializers(serializers.ModelSerializer):
    addressddet = AddressModelSerializers(source='address',
        many=False,
        read_only=True,
    )
    class Meta:
        model = User
        fields ="__all__"


class BookingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingProduct
        fields = "__all__"
        depth = 1


class BookingModelSerializers(serializers.ModelSerializer):
    booking_products = serializers.SerializerMethodField()
    payble_amount = serializers.SerializerMethodField()
    formatted_start_time = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = "__all__"
        depth = 1

    def get_booking_products(self, obj):
        booking_products = BookingProduct.objects.filter(booking=obj)
        return BookingProductSerializer(booking_products, many=True).data

    def get_payble_amount(self, obj):
        booking = BookingProduct.objects.filter(booking=obj)
        payble_amount =0
        for b in booking:
            payble_amount += b.product.dis_price * b.quantity
        return payble_amount
    
    def get_formatted_start_time(self, obj):
        if obj.time_slot and obj.time_slot.start_time:
            return obj.time_slot.start_time.strftime('%I:%M %p')
        return None

    

class RejectReasonSerializers(serializers.ModelSerializer):

    class Meta:
        model =RejectReason
        fields = ['title']