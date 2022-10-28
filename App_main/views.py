from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination

from App_main.models import *
from App_main.serializers import *

# Create your views here.
class IsPostAdmin(permissions.BasePermission):
    def has_permission(self, request, obj):
        if request.user and obj.owner:
            return True


@api_view(['POST'])
def post_api_get_view(request):
    if request.method == 'POST':
        return Response('')
    

class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class PostAPIView(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsPostAdmin]
    
    pagination_class = MyPagination
    filter_backends = [filters.OrderingFilter]
    ordering = ['-upload_date']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    @action(detail = True)
    def get_user_posts(self, request, pk=None):
        owner = get_object_or_404(CustomUser, pk=pk)
        owner_posts = PostModel.objects.filter(owner=owner.id)
        serializer = PostModelSerializer
        return Response(serializer.data)


class HomePostAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class AddNewPostAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikePostAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = LikeModel.objects.all()
    serializer_class = LikeModelSerializer
    
    # lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def create(self ,request , pk=None):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        post_id = get_object_or_404(PostModel, id=request.data['post'])
        serializer.save(user = self.request.user, post = post_id)
        return Response({"Success": "Liked"})
    

@api_view(['DELETE'])
def unlikeAPIView(request, post_id):
    liked = LikeModel.objects.get(post=PostModel.objects.get(id=post_id))
    if liked.user == request.user:
        liked.delete()
        return Response({"Success": "deleted"})
    else:
        return Response({"Error": "Unlike not possible"})
