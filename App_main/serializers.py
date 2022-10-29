from rest_framework import serializers
from .models import PostModel, LikeModel, CommentModel

from  App_login.models import *


class OnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email']
    

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id', 'post_text', 'post_author']
        read_only_fields = ['post_author']

        
    # def get_author(self, postAuthor):
    #     return OnlyUserSerializer(postAuthor.author).data


class LikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        exclude = ['post', 'user', 'like_created']


class CommentCreateSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta():
        model = CommentModel
        fields = 'all'
        read_only_fields = ['post', 'user', 'comment_date']

    def get_owner(self ,obj):
        return OnlyUserSerializer(obj.user).data
