from django.shortcuts import render


# homepage
def homepage(request):

    return render(request, 'pages/me.html')
