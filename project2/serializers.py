from rest_framework import serializers
from .models import user,Nokta

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
        
class noktaSerializer(serializers.ModelSerializer):
    class Meta:
        model2 = Nokta
        fields = '__all__'