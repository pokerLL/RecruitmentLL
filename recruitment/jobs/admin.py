from django.contrib import admin

# Register your models here.

# from jobs.utils import actions  as myaction
from utils.actions import jobs as myaction
from jobs.models import Resume


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', "username", 'has_goto_interview',
                    "gender", 'city', 'phone', "apply_position", ]
    # 右侧筛选条件
    list_filter = ('gender', 'city', 'apply_position', "has_goto_interview")

    # 查询字段
    search_fields = ('username', 'phone')

    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_actions(self, request):
        actions = super().get_actions(request)
        group_names = self.get_group_names(request.user)
        print(actions)
        print(type(actions))
        if request.user.is_superuser or "AdminManager" in group_names:
            actions['goto_interview'] = (
                myaction.goto_interview, "goto_interview", "进入面试流程")
            pass
        return actions


admin.site.register(Resume, ResumeAdmin)
