from django.shortcuts import render
from .models import TechSkills, GeneralSkills, WorkExperience, WorkDescriptions, Education
import json
from django.forms.models import model_to_dict
import decimal


# homepage
def homepage(request):

    return render(request, 'pages/me.html')


# skills testing page
def show_skills(request):

    all_skills = TechSkills.objects.all().order_by('name')
    skills = []
    for s in all_skills:
        add = model_to_dict(s)
        skills.append(add)

    context = {
        'skills': json.dumps(skills)
    }

    return render(request, 'pages/skills.html', context)


# resume page
def show_resume(request):

    # call all the objects
    techs = TechSkills.objects.all().order_by('name')
    gens = GeneralSkills.objects.all().order_by('name')
    edus = Education.objects.all().order_by('-end_year')
    works = WorkExperience.objects.all().order_by('-start_year')
    workds = WorkDescriptions.objects.all()

    # declare lists
    tech_skills = []
    gen_skills = []
    education = []
    work_exp = []
    work_desc = []

    # convert all models to dict for JSON
    for t in techs:
        add = model_to_dict(t)
        tech_skills.append(add)
    for g in gens:
        add = model_to_dict(g)
        gen_skills.append(add)
    for e in edus:
        add = model_to_dict(e)
        education.append(add)
    for w in works:
        add = model_to_dict(w)
        work_exp.append(add)
    for d in workds:
        add = model_to_dict(d)
        work_desc.append(add)

    context = {
        'tech_skills': json.dumps(tech_skills),
        'gen_skills': json.dumps(gen_skills),
        'education': json.dumps(education),
        'work_exp': json.dumps(work_exp),
        'work_desc': json.dumps(work_desc)
    }

    return render(request, 'pages/resume.html', context)
