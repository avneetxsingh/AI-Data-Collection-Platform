# from django.shortcuts import render
# from django.views import View
# from http import HttpR
# from .models import *
# Create your views here.
# def home(request):
#     student_details=Student.objects.all()
#     return render(request,"index.html")
# def home_post(request):
#     if request.method == "POST":
#         std_name=request.POST.get("student_name")
#         Student(name = std_name).save()
#         obj = Student.objects.get(id=1)
#         print(obj)
#         return render(request,"index.html")

# from django.views import View
# from django.shortcuts import render
# from App.models import Question

# class Home(View):
#     def get(self, request):
#         topics = Question.objects.values('query_type').distinct()
#         context = {'topics': topics}
#         return render(request, "index.html", context)

#     def post(self, request):
#         soft_answ = request.POST.get("softage_answer")
#         print("------->>>>>>>", soft_answ)
#         question = Question(query_type=soft_answ)
#         question.save()
#         return render(request, "index.html")

from django.views import View
from django.shortcuts import render
from .models import Question

class Home(View):
    def get(self, request):
        topics = Question.objects.values('query_type').distinct()
        dd = request.POST.get("dropdown")
        print("---------->>>>>",dd)
        questions = Question.objects.filter(query_type = dd).all()
        context = {'topics': topics, 'questions': questions}
        return render(request, "index.html", context)

    def post(self, request):
        soft_answ = request.POST.get("softage_answer")
        print("------->>>>>>>", soft_answ)
        question = Question(query_type=soft_answ)
        question.save()
        return render(request, "index.html")