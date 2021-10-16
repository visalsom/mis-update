from rest_framework import serializers
from api.models import Document, Soldier



class SoldierSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only= True)
    class Meta:
        model= Soldier
        fields = ['id', 'user_id', 'rcaf_id', 'phone_number', 'birth_date' ]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields= ['id', 'doc_type', 'name', 'title', 'objective', 'reference', 'body','end_body']