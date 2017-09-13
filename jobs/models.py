from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


def validate_class(grad_class):
    year_number = grad_class // 100
    class_number = grad_class % 100
    if not (100000 <= grad_class <= 999999):
        raise ValidationError(_('班级号应为6位整数'), params={'grad_class': grad_class})
    if year_number < 1958:
        raise ValidationError(_('毕业年份不合法'), params={'year_number': year_number})
    if class_number == 0:
        raise ValidationError(_('班级号不能为0'), params={'class_number': class_number})


@python_2_unicode_compatible
class Job(models.Model):

    class Meta:
        ordering = ['-date_published']
        verbose_name = _('职位')
        verbose_name_plural = _('职位')

    INTERN = 'INTERN'
    SOCIAL = 'SOCIAL'

    TYPE_CHOICES = [
        (INTERN, _('实习')),
        (SOCIAL, _('社招')),
    ]

    published = models.BooleanField(
        default=False,
        verbose_name=_('已发布')
    )

    date_published = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('发布时间'),
        editable=False
    )

    times_viewed = models.IntegerField(
        default=0,
        verbose_name=_('已查看次数')
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        default=INTERN,
        verbose_name=_('招聘类型')
    )

    company = models.CharField(
        max_length=50,
        help_text=_('如 “Google” 或 “上海中学”'),
        verbose_name=_('单位名称')
    )

    location = models.CharField(
        max_length=50,
        help_text=_('如 “上海” 或 “Mountain View, CA”'),
        verbose_name=_('工作城市')
    )

    job_position = models.CharField(
        max_length=50,
        help_text=_('如 “软件工程师”'),
        verbose_name=_('招聘职位')
    )

    department = models.CharField(
        max_length=50,
        help_text=_('如 “人力资源部”'),
        verbose_name=_('工作部门')
    )

    publisher_class = models.SmallIntegerField(
        help_text=_('请填写六位班级号（四位毕业年份+两位班级号），如 “201602”'),
        default=195801,
        verbose_name=_('发布者班级'),
        validators=[validate_class]
    )

    publisher = models.CharField(
        max_length=50,
        help_text=_('请填写姓名'),
        verbose_name=_('发布者')
    )

    salary = models.CharField(
        max_length=50,
        help_text=_('如 “10000元/月”'),
        verbose_name=_('薪资')
    )

    submitting_resume = models.CharField(
        max_length=300,
        help_text='如 “发送简历至 hr@google.com”',
        verbose_name=_('简历递交方式')
    )

    description = models.TextField(
        verbose_name=_('工作描述')
    )

    requirements = models.TextField(
        verbose_name=_('招聘要求')
    )

    company_description = models.TextField(
        verbose_name=_('单位介绍')
    )

    def __str__(self):
        return self.job_position + " at " + self.department + ", " + self.company + " in " + self.location

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'pk': self.pk})

    def get_publisher_grad_year(self):
        return self.publisher_class // 100

    def get_publisher_grad_class(self):
        return self.publisher_class % 100
