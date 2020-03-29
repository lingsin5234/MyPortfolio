from django.contrib import admin
from .models import TechSkills, GeneralSkills, Education, WorkExperience, WorkDescriptions, Hobbies
from .models import ContactMe, Qualifications, ProjectExperience


admin.site.register(TechSkills)
admin.site.register(GeneralSkills)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(WorkDescriptions)
admin.site.register(Hobbies)
admin.site.register(ContactMe)
admin.site.register(Qualifications)
admin.site.register(ProjectExperience)
