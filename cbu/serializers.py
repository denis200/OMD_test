from rest_framework import serializers
from .models import CBUData


class CBUDataSerializer(serializers.ModelSerializer):
    reach = serializers.ListField(
        child=serializers.DecimalField(
            max_digits=5, 
            decimal_places=2, 
            min_value=0, 
            max_value=100
        ),
        min_length=2,
        max_length=2
    )

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(CBUDataSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = CBUData
        fields = ['unit','reach']

"""
{
"user_table":1,
"unit":1,
"reach":[1,2]
}
"""