from dataclasses import field
from wsgiref import validate
from django.conf import settings
from rest_framework import serializers
from api.models import Department, Document, Send, Soldier, Subdepartment, Unit

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
    
    def create(self, validated_data):
        soldier = Soldier(**validated_data)
        soldier.user_id = self.context['user_id']
        soldier.save()
        return soldier

class SoldierSerializer(CreateSoldierSerializer):
    unit =UnitSerializer(many=False)
    class Meta(CreateSoldierSerializer.Meta):
        fields = ['id', 'user_id', 'rcaf_id', 'phone_number', 'birth_date','address', 'unit' ] 

class DocumentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only= True)
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

class SendDocumentSerializer(serializers.ModelSerializer):
    document_id= serializers.UUIDField()
    destination_soldier= serializers.IntegerField()
    class Meta:
        model= Send
        fields= ['id', 'destination_soldier', 'document_id']

    def validate(self, attrs):
        soldier = Soldier.objects.only('id').get(user_id= attrs['destination_soldier'])
        document = Document.objects.only('id').get(id = attrs['document_id'])
        if not soldier:
            raise serializers.ValidationError('User Does not exits')
        elif soldier == self.context['user_id']:
            raise serializers.ValidationError('You already have This Document')
        elif not document.id:
            raise serializers.ValidationError('Document Does not exist')
        return attrs

    