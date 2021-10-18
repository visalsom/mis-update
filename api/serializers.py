from dataclasses import field
from rest_framework import serializers
from api.models import Department, Document, Soldier, Subdepartment, Unit

class SubdepartmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Subdepartment
        fields = ['id', 'name', 'location']

class DepartmentSerializer(serializers.ModelSerializer):
    subdepartment = SubdepartmentSerializer(many = False)
    class Meta:
        model = Department
        fields = ['id', 'name', 'location', 'subdepartment' ]

class UnitSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False)
    class Meta :
        model = Unit
        fields = ['id', 'name', 'location', 'department']

class CreateSoldierSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only= True)
    class Meta:
        model= Soldier
        fields = ['id', 'user_id', 'rcaf_id', 'phone_number', 'birth_date','address' ]

class SoldierSerializer(CreateSoldierSerializer):
    unit =UnitSerializer(many=False)
    class Meta(CreateSoldierSerializer.Meta):
        fields = ['id', 'user_id', 'rcaf_id', 'phone_number', 'birth_date','address', 'unit' ] 

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields= ['id', 'doc_type', 'name', 'title', 'objective', 'reference', 'body','end_body']

    def create(self, validated_data):
        document = Document(**validated_data)
        soldier = Soldier.objects.get(user_id = self.context['user_id'])
        document.soldier_id = soldier.id
        document.save()
        return document
        
class UpdateDocumentSerializer(DocumentSerializer):
    class Meta(DocumentSerializer.Meta):
        fields= ['id', 'name', 'title', 'objective', 'reference', 'body','end_body']
        