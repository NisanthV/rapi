from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# class RegisterAuthenticate(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','username','password']
#         extra_kwargs={"password":{"write_only":True}}
#
#     def create(self, validated_data):
#         user=User.objects.create_user(**validated_data)
#         return user

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=['id','title','content','price','sale','my_discount']

    def get_my_discount(self,obj):
            # if not hasattr(obj, 'id'):
            #     return None
            # if not isinstance(obj, Product):
            #     return None
            try:
                return obj.discount()
            except:
                return None
