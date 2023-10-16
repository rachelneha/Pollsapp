from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Choice
from django.urls import reverse
from django.views.generic import ListView,DetailView


# Create your views here.
class displayQuestionView(ListView):
    model = Questions
    template_name =  "polls/index.html"

    def get_queryset(self):
        return Questions.objects.order_by("-pub_date")[:5]
# def display(request):
#     latest = Questions.objects.order_by("-pub_date")[:5]
#     context ={"latest":latest}
#     # output = ", ".join([q.question for q in latest])
#     return render(request,"polls/index.html",context)


class DetailQuestionView(DetailView):
    model = Questions
    template_name = "polls/details.html"
    context_object_name = "ques"

# def detail(request, question_id):
#     # try:
#     #     ques = Questions.objects.get(pk = question_id)
#     # except Questions.DoesNotExist:
#     #     raise Http404("Question doesnot esxit")
#     ques = get_object_or_404(Questions,pk = question_id)
#     context = {"ques":ques}
#     return render(request,"polls/details.html",context)


def vote(request, question_id):
    quest = get_object_or_404(Questions , pk =question_id)
    try:
        selected = quest.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        context ={
            "ques" : quest,
            "error_message" :"You dont fill up a choice"
        }
        return render(request,'polls/details.html', context)
    else:
        selected.votes +=1
        selected.save()
        return HttpResponseRedirect(reverse("polls:result", kwargs={"pk":quest.id}))

class ResultOfVote(DetailView):
    model = Questions
    template_name = "polls/output.html"
    context_object_name = "q"

# def ResultOfVote():
#     q = get_object_or_404(Questions,pk= question_id)
#     return render(request,'polls/output.html',{'q':q})



