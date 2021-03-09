from django.shortcuts import render

def index(request):
    template_path = 'webfront/index.html'
    context = {}
    return render(request, template_path, context)


def detail(request, question_id):
    template_path = 'webfront/detail.html'
    context = {"question_id":question_id}
    return render(request, template_path, context)
