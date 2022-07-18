from interview.models import Candidate

def goto_interview(modeladmin, request, queryset):
    for obj in queryset:
        obj.has_goto_interview = True
        obj.save()
        candidate = Candidate()
        candidate.username = obj.username
        candidate.city = obj.city
        candidate.phone = obj.phone
        candidate.email = obj.email
        candidate.apply_position = obj.apply_position
        candidate.from_address = obj.from_address
        candidate.gender = obj.gender
        candidate.bachelor_school = obj.bachelor_school
        candidate.master_school = obj.master_school
        candidate.doctor_school = obj.doctor_school
        candidate.major = obj.major
        candidate.degree = obj.degree
        candidate.save()
        