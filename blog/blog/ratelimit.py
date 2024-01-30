from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

@ratelimit(key='user', rate='5/m', method='GET', block=True)
def my_view(request):
    # ваш код представления
    return render(request, 'my_template.html')
