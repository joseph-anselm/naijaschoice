from django.db.models.fields import SlugField
from django.forms.models import ModelForm
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from .models import Question, Choice, Comments
from django.urls import reverse
from django.views.generic.list import ListView
from .forms import CommentForm


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')
    paginator = Paginator(latest_question_list, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator. get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'polls/index.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    comments = question.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # data = form.save(commit=False)
            # data.question = question
            # data.save()
            # return redirect('results', pk=question_id)

            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.question = question
            # Save the comment to the database
            new_comment.save()

    else:
        form = CommentForm()
    return render(request, 'polls/results.html', {'question': question,
                                                  'form': form, 'new_comment': new_comment, 'comments': comments})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# def polldetail(request, question_id):
#     template_name = 'polls/polldetail.html'
#     post = get_object_or_404(Question, pk=question_id)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.question = comments
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         form = CommentForm()
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'form': form})


def search_polls(request):
    query = request.GET.get('p')
    object_list = Question.objects.filter(tags__icontains=query)
    context = {
        'posts': object_list,
    }
    return render(request, "polls/search_polls.html", context)
