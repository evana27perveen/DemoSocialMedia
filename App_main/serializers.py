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
        fields = ['id', 'post_text']

        
    # def get_author(self, postAuthor):
    #     return OnlyUserSerializer(postAuthor.author).data


class LikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        exclude = ['post', 'user', 'like_created']


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        exclude = ['post', 'user', 'comment_created']
