from django.shortcuts import render

# Create your views here.
def some_function(request):
    context = {
        "msg": "Hello World!",
        "msg2": "this is my second test",
        "msg3":"this worked",
    }
    return render(request, 'task_2_view.html', context)