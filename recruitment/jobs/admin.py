from django.contrib import admin
from django.utils.html import format_html



from jobs.models import Resume,Picture,Attachment
# from jobs.utils import actions  as myaction
from utils.actions import jobs as myaction

# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', "username", 'has_goto_interview','image_tag',
                    "gender", 'city', 'phone', "apply_position", 'attachment_tag']
    # 右侧筛选条件
    list_filter = ('gender', 'city', 'apply_position', "has_goto_interview")

    # 查询字段
    search_fields = ('username', 'phone')
    
    @admin.display(description='照片')
    def image_tag(self, obj):
        if not obj.picture:
            return "-"
        _picture = Picture.objects.get(id=obj.picture.id).file
        print(_picture)
        if _picture:
            return format_html('<a href="{0}" target="_blank"><img src="{0}" style="width:100px;height:80px;"/></a>'.format(_picture.url))
    
    @admin.display(description='简历')
    def attachment_tag(self, obj):
        if not obj.attachment:
            return "-"
        _attachment = Attachment.objects.get(id=obj.attachment.id).file
        if _attachment:
            return format_html('<a href="{0}" target="_blank">{1}</a>'.format(_attachment.url,_attachment.name.split("/")[1]))

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
