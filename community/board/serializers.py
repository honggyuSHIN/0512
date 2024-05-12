from rest_framework import serializers
from .models import Board,Comment
from django.utils import timezone



class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model=Board
        fields=['id','title','body']
        



class PostResponseSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    
    class Meta:
        model=Board
        fields=['id','title','body','created_at']

    def get_created_at(self,obj):
        time=timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')



class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields=['id','title','body']

        

class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields=['title','body']



class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['comment']

class CommentResponseSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['id','post','created_at','comment']

    def get_created_at(self,obj):
        time=timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')



class PostDetailSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    comments=CommentResponseSerializer(many=True,read_only=True)

    class Meta:
        model=Board
        fields=['id','title','body','created_at','comments']
    
    def get_created_at(self,obj):
        time=timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')









# class BoardSerializer02(serializers.ModelSerializer):
#     class Meta:
#         model=Board

#         fields=['id','title','body','created_at']








        
        
        
        
        
        
        






