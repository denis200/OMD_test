from rest_framework import serializers
from .models import CBUData


class CBUDataSerializer(serializers.ModelSerializer):
    reach = serializers.ListField(
        child=serializers.FloatField(
            min_value=0.0, 
            max_value=100.0
        ),
        allow_empty=False,
        min_length=10,
        max_length=10
    )

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(CBUDataSerializer, self).__init__(many=many, *args, **kwargs)
    
    def validate_reach(self, value):    
        print(value)
        for idx in range(len(value)-1):
            if value[idx] < value[idx+1]:
                raise serializers.ValidationError(
                    "The array must be sorted in descending order"
                )
        return value

    class Meta:
        model = CBUData
        fields = ['unit','reach']