from django.db import models
from django.conf import settings

# Create your models here.

class Soldier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    rcaf_id  = models.CharField(max_length= 6)
    phone_number = models.CharField(max_length=13)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    

class Document(models.Model):
    DOCUMENT_DOCUMENT = 'D'
    DOCUMENT_ANNOUNCEMENT = 'A'
    DOCUMENT_CHOICES = [
        (DOCUMENT_DOCUMENT, 'Document'),
        (DOCUMENT_ANNOUNCEMENT, 'Announcement')
    ]
    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    objective = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    end_body = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=1, choices=DOCUMENT_CHOICES, default=DOCUMENT_DOCUMENT)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name', 'doc_type']


