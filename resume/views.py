from django.shortcuts import render
from .models import TechSkills
import json
from django.forms.models import model_to_dict
import decimal


# homepage
def homepage(request):

    return render(request, 'pages/me.html')


# skills testing page
def show_skills(request):

    all_skills = TechSkills.objects.all()
    skills = []
    for s in all_skills:
        add = model_to_dict(s)
        skills.append(add)

    context = {
        'skills': json.dumps(skills)
    }

    return render(request, 'pages/skills.html', context)
