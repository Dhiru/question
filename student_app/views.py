from student_app.models import Question, Answer, User, Tenant
from rest_framework import viewsets
from rest_framework.response import Response


class QuestionViewSet(viewsets.ViewSet):

    def list(self, request):
        Questions = Question.objects.filter(private=False)
        qu = {}
        li = []
        for each in Questions:
            q = dict()
            q['question'] = each.title
            answer = Answer.objects.filter(question_id__id=each.id)
            if answer is not None:
                ans = answer[0]
                q['answer'] = ans.body
            else:
                q['answer'] = ""
            li.append(q)
        qu['questions'] = li
        return Response(qu, status=200)

