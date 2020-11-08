from django.shortcuts import render
from .models import TechSkills, GeneralSkills, WorkExperience, WorkDescriptions, Education
from .models import Qualifications, ProjectExperience
import json
from django.forms.models import model_to_dict
from .forms import CaptchaContactForm
import decimal
from django.template.loader import select_template, get_template
from djangoapps.settings import BASE_DIR
from djangoapps.utils import get_this_template


# homepage - ###### DEFUNCT #######
def homepage(request):

    # give temporary data for projects
    projects = [
        {'id': 1, 'name': 'Resume', 'img': 'static/img/writing.jpg', 'link': 'resume/'},
        {'id': 2, 'name': 'Baseball', 'img': 'static/img/baseball.jpg', 'link': 'baseball/'},
        {'id': 3, 'name': 'Budget Demo', 'img': 'static/img/piggybank.jpg', 'link': 'budget/'},
        {'id': 4, 'name': 'Wordpress - Softball Team', 'img': 'static/img/looneytoons.jpg',
            'link': 'https://looneytoons.sinto-ling.ca'},
        {'id': 5, 'name': 'Coming Soon!', 'img': 'static/img/noaa.jpg', 'link': '/'},
        # {'id': 7, 'name': 'Wordpress - My Travels', 'img': 'static/img/looneytoons.jpg',
        #  'link': 'https://travel.sinto-ling.ca'},
    ]

    context = {
        'projects': json.dumps(projects)
    }

    return render(request, 'pages/me.html', context)


# projects list
def projects_list(request):

    # give temporary data for projects
    projects = [
        {'id': 1, 'name': 'Resume', 'img': '/static/img/writing.jpg', 'link': '/resume/'},
        {'id': 2, 'name': 'Baseball', 'img': '/static/img/baseball.jpg', 'link': '/baseball/'},
        {'id': 3, 'name': 'Weather', 'img': '/static/img/noaa.jpg', 'link': '/gsod/'},
        {'id': 4, 'name': 'Tutorials', 'img': '/static/img/tutorial.jpg', 'link': '/tutorials/'},
        {'id': 5, 'name': 'Udemy Courses', 'img': '/static/img/coding.jpg', 'link': '/udemy/'},
        {'id': 6, 'name': 'Canada Open Data', 'img': '/static/img/canada-bike.jpg', 'link': '/statscan/'},
        # {'id': 7, 'name': 'Budget Demo', 'img': '/static/img/piggybank.jpg', 'link': '/budget/'},
    ]

    blogs = [
        {'id': 1, 'name': 'Wordpress - Softball Team', 'img': '/static/img/looneytoons.jpg',
         'link': 'https://looneytoons.sinto-ling.ca'},
        {'id': 2, 'name': 'My Travels', 'img': '/static/img/travels.gif', 'link': 'https://travel.sinto-ling.ca'}
    ]

    context = {
        'projects': json.dumps(projects),
        'blogs': json.dumps(blogs)
    }

    return render(request, 'pages/projectList.html', context)


# about me page
def about_me(request):

    return render(request, 'pages/aboutMe.html')


# contact me page
def contact_me(request):

    form = CaptchaContactForm()

    if request.method == 'POST':
        form = CaptchaContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Success")

    context = {
        'form': form
    }

    return render(request, 'pages/contactMe.html', context)


# project page
def project_markdown(request):

    page_height = 1050
    f = open('resume/README.md', 'r')
    if f.mode == 'r':
        readme = f.read()
        page_height = len(readme) - 325

    content = {
        'readme': readme,
        'page_height': page_height
    }

    template_page = get_this_template('resume', 'project.html')

    return render(request, template_page, content)


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
    techs = TechSkills.objects.all().order_by('order')
    gens = GeneralSkills.objects.all().order_by('name')
    edus = Education.objects.all().order_by('-end_year')
    works = WorkExperience.objects.all().order_by('-start_year')
    workds = WorkDescriptions.objects.all().order_by('id')
    quali = Qualifications.objects.all().order_by('order')
    proj = ProjectExperience.objects.all().order_by('-start_year', '-start_month')

    # declare lists
    tech_skills = []
    gen_skills = []
    education = []
    work_exp = []
    work_desc = []
    qualification = []
    projects = []

    # find max desc for work and proj
    max_work_desc = 0
    max_proj_desc = 0

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
    for q in quali:
        add = model_to_dict(q)
        qualification.append(add)
    for p in proj:
        add = model_to_dict(p)
        indv_wd = add['description']
        if len(indv_wd) > max_proj_desc:
            max_proj_desc = len(indv_wd)
        projects.append(add)

    # special treatment for work_desc and work_exp
    for d in workds:
        add = model_to_dict(d)
        work_desc.append(add)
    # for each work_exp, match the work_descs available
    for w in works:
        add = model_to_dict(w)
        # create a list of work_desc
        indv_wd = [d['description'] for d in work_desc if d['job'] == w.id]
        if len(indv_wd) > 0:
            add['work_desc'] = indv_wd
            if len(indv_wd) > max_work_desc:
                max_work_desc = len(indv_wd)
        else:
            add['work_desc'] = [""]
        work_exp.append(add)

    context = {
        'tech_skills': json.dumps(tech_skills),
        'gen_skills': json.dumps(gen_skills),
        'education': json.dumps(education),
        'work_exp': json.dumps(work_exp),
        'work_desc': json.dumps(work_desc),
        # 'qualification': json.dumps(qualification),
        'projects': json.dumps(projects),
        'max_work_desc': max_work_desc,
        'max_proj_desc': max_proj_desc
    }

    return render(request, 'pages/portfolio.html', context)


# show work exp test view
def show_workexp(request):

    all_work_exp = WorkExperience.objects.all()
    all_work_desc = WorkDescriptions.objects.all()

    # next change all work_description to dict
    dict_wd = []
    for wd in all_work_desc:
        obj = model_to_dict(wd)
        dict_wd.append(obj)

    # go through each work exp and add the corresponding work_descriptions
    dict_we = []
    for we in all_work_exp:
        obj = model_to_dict(we)
        indv_wd = [wd['description'] for wd in dict_wd if wd['job'] == we.id]
        if len(indv_wd) > 0:
            obj['work_desc'] = indv_wd
        else:
            obj['work_desc'] = [""]  # create a blank array still.
        dict_we.append(obj)

    work_exp = all_work_exp
    work_desc = all_work_desc

    context = {
        'work_exp': work_exp,
        'work_desc': work_desc,
        'dict_we': json.dumps(dict_we),
        'dict_wd': dict_wd
    }

    return render(request, 'pages/work_exp.html', context)


# blank view
def blank(request):

    return render(request, 'pages/multidimensionarray.html')


# template testing
def django_templates(request):

    temp1 = get_template('pages/project.html')
    temp2 = select_template(['pages/project.html'])
    print(type(temp1))
    # print(temp1.app_dirname)
    print(type(temp2))
    print(BASE_DIR)

    context = {
        'temp1': temp1,
        'temp2': temp2
    }

    return render(request, 'pages/django_templates.html', context)


# photo credits page
def photo_credits(request):

    page_height = 1050
    f = open('resume/PhotoCredits.md', 'r')
    if f.mode == 'r':
        readme = f.read()
        page_height = len(readme)

    content = {
        'readme': readme,
        'page_height': page_height
    }

    template_page = get_this_template('resume', 'photo-credits.html')

    return render(request, template_page, content)
