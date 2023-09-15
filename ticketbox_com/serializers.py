from rest_framework.serializers import ModelSerializer
from .models import *



class TgChannelSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TicketBoxEvent


