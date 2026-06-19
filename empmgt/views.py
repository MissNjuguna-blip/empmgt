from django.http import HttpResponse
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("Welcome to django")

def introduction (request):
    return HttpResponse("The new Url for views")

@api_view(['POST'])
def add(request):
    num1 = request.data.get('num1')
    num2=request.data.get('num2')
    sum=num1+num2
    return HttpResponse(f"Sum of {num1} and {num2} is: {sum}")