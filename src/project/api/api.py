from django.http import Http404

from project.api.serializers import QuestionSerializer
from project.polls.model import Question
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class QuestionAPIView(views.APIView):
    http_method_names = ('get', 'put')
    permission_classes = (IsAuthenticated,)


    """
       @api {get} /api/question/<pk>
       @apiName Question
       @apiDescription Get Question information
       @apiGroup Question

       @apiSuccessExample {json} Success-Response:
         HTTP/1.1 200 OK
       {
           "id": 123312321,
           "question_text": "Example question"
           "pub_date": "2017-03-12T12:49:30.924000Z"
        }
   """



    def get_object(self):
        question = Question.objects.get(pk=self.kwargs['pk'])
        return question

    def get(self, request, pk=None):
        if pk is not None:
            question = self.get_object()
            return Response(QuestionSerializer(question).data)
        raise Http404

    def put(self, request, *args, **kwargs):
            serializer = QuestionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

