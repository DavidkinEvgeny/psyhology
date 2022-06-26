from django.shortcuts import redirect, render
from django.views.generic import DeleteView, ListView
from .forms import QuestionForm
from .models import MyQuesyion


def add_user_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("questions:result_user_question", form.id)
    else:
        form = QuestionForm()
    return render(request, "questions/item.html", {"form": form})


def result_user_question(request, id):
    pass


class ResultDetailView(DeleteView):
    model = MyQuesyion
    template_name = "questions/result.html"
    context_object_name = "result"


class ResultListView(ListView):
    model = MyQuesyion
    template_name = "questions/results.html"
    # context_object_name = "result"
