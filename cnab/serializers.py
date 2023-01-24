from rest_framework import serializers

class CNABSerializer(serializers.ModelSerializer):
    # é necessário passar o pefil e o seu serializador
   
    def create(self, validated_data):
        return ''