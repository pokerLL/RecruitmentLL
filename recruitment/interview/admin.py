from django.contrib import admin
from django.db.models import Q
from interview import admin_fields
from interview.models import Candidate
from utils.actions import interview as myaction


# Register your models here.
# 面试官只能看到自己的面试对象的资料和自己要填写的部分（以及之前面的评价，但无权修改）
# 所有面试官可以看到所有简历
# 只有管理员可以让简历进入面试流程以及指定面试官


class InterviewerAdmin(admin.ModelAdmin):
    list_display = ["username", "gender", "phone", "test_score_of_general_ability", "paper_score",
                    "first_interviewer_user",
                    "first_result", "second_interviewer_user", "second_result", "hr_interviewer_user", "hr_result"]
    # 右侧筛选条件
    list_filter = ('city', 'first_result', 'second_result', 'hr_result',
                   'first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user')

    # 查询字段
    search_fields = ('username', 'phone', 'email')

    # 列表页排序字段
    ordering = ('hr_result', 'second_result', 'first_result',)

    actions = (myaction.export_model_as_csv, myaction.notify_interviewer,)

    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_fieldsets(self, request, obj):
        group_names = self.get_group_names(request.user)
        if 'Interviewer' in group_names and obj.first_interviewer_user == request.user:
            return admin_fields.default_fieldsets_first
        if 'Interviewer' in group_names and obj.second_interviewer_user == request.user:
            return admin_fields.default_fieldsets_second
        if 'Interviewer' in group_names and obj.hr_interviewer_user == request.user:
            return admin_fields.default_fieldsets
        return admin_fields.default_fieldsets

    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)
        if 'Interviewer' in group_names and obj.first_interviewer_user == request.user:
            return admin_fields.readonly_fields_first
        if 'Interviewer' in group_names and obj.second_interviewer_user == request.user:
            return admin_fields.readonly_fields_second
        if 'Interviewer' in group_names and obj.hr_interviewer_user == request.user:
            return admin_fields.readonly_fields_hr
        return []

    def get_queryset(self, request):
        qs = super(InterviewerAdmin, self).get_queryset(request)
        user = request.user
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'AdminManager' in group_names:
            return qs
        return Candidate.objects.filter(
            Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user) | Q(
                hr_interviewer_user=request.user))

    def get_changelist_instance(self, request):

        self.list_editable = self.get_list_editable(request)
        return super(InterviewerAdmin, self).get_changelist_instance(request)

    # 这个函数Django并不提供
    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'AdminManager' in group_names:
            return ('first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user')
        return ()

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator:
            obj.creator = request.user.username
        obj.save()


admin.site.register(Candidate, InterviewerAdmin)
