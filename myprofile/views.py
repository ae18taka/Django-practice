from django.shortcuts import render

# Create your views here.
def top(request):
    context = {
        'name' : 'たかあき'
    }

    return render(request,'myprofile/top.html',context)

def resume(request):
    context = {
        'school' : '九州大学大学院'
    }

    return render(request,'myprofile/resume.html')