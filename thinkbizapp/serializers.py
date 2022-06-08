from rest_framework import serializers
from thinkbizapp.models import *


class educators(serializers.ModelSerializer):
    class Meta:
        model=Educator
        fields=('id','first_name','last_name','course','email','contact')