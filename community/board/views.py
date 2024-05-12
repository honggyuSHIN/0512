from .models import Board
from .serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def board_list(request):
    if request.method=='GET':
        boards=Board.objects.all()

        
        # django ORM을 사용하여 데이터베이스에서 모든 Board
        # 객체를 가져오는 쿼리
        # .objects는 모든 Django 모델의 기본 메니저임.
        # -> 데이터베이스에 대한 쿼리를 수행할 수 있음.
        # .all()은 매니저를 통해 모든 객체를 가져오는 메서드임.

        serializer=PostListSerializer(boards,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)



        



@api_view(['POST'])
def board_third(request):
    if request.method=='POST':
        serializer=PostRequestSerializer(data=request.data)

        if serializer.is_valid():
            post=serializer.save()
            response=PostResponseSerializer(post)
            return Response(response.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def board_detail(request, pk):
    try: 
        board = Board.objects.get(pk=pk)
        if request.method=='GET':
            serializer = PostDetailSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)

    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def create_comment(request,post_id):
    post=Board.objects.get(pk=post_id)

    if request.method=='POST':
        serializer=CommentRequestSerializer(data=request.data)

        if serializer.is_valid():
            comment=serializer.save(post=post)
            response=CommentResponseSerializer(comment)
            return Response(response.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def board_fix(request,pk):
    try: 
        board = Board.objects.get(pk=pk)
        if request.method=='PUT':
            serializer=PostRequestSerializer(board,data=request.data)

            if serializer.is_valid():
                post=serializer.save()
                response=PostResponseSerializer(post)
                return Response(response.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def board_delete(request,pk):
    try:
        board = Board.objects.get(pk=pk)
        if request.method=='DELETE':
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_comments(request,post_id):
    post=Board.objects.get(pk=post_id)
    comments=Comment.objects.filter(post=post)
    serializer=CommentResponseSerializer(comments,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



