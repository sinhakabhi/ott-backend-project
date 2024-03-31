# ott_app/viewership/serializers.py
from rest_framework import serializers
from .models import Customer, Viewership


class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer Serializer Class
    """

    class Meta:
        model = Customer
        fields = ["id", "name", "password"]

    def create(self, validated_data):
        """
        Overriding create() method

        Args:
            validated_data (JSON): Customer fields

        Returns:
            Obj: Customer Object
        """
        customer = Customer.objects.create(
            id=validated_data["id"], name=validated_data["name"]
        )
        customer.set_password(validated_data["password"])
        customer.save()
        return customer


class ViewershipSerializer(serializers.ModelSerializer):
    """
    Viewership Serializer Class
    """

    class Meta:
        model = Viewership
        fields = ["timestamp", "video_title"]
