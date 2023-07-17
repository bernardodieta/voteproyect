from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {"latest_question_list":latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    quesiton = get_object_or_404(Question, pk=question_id)
    return render (request, "polls/results.html", {
        "question": quesiton
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "question": question,
            "error_message": "no elegiste una respuesta"
        } )
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))