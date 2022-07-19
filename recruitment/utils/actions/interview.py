from django.contrib import admin
from django.http import HttpResponse
from datetime import datetime
import csv

# from utils.dingtalk import send_message
from interview.tasks import send_dingtalk_message

exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
                     'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')


@admin.action(description='导出所选项为CSV文件')
def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title()
         for f in field_list],
    )

    for obj in queryset:
        # 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)
    return response


# 通知面试官面试
@admin.action(description='通知面试官面试')
def notify_interviewer(modeladmin, request, queryset):
    for obj in queryset:
        candidate = obj.username
        first_interviewer = obj.first_interviewer_user.username
        second_interviewer = obj.second_interviewer_user.username
        hr_interviewer = obj.hr_interviewer_user.username
        msg = "候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s ; %s ; %s ." % (
            candidate, first_interviewer, second_interviewer, hr_interviewer)
        print(msg)
        send_dingtalk_message.delay(msg)
        # send_message("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s ; %s ; %s ." %
        #              (candidate, first_interviewer, second_interviewer, hr_interviewer))
