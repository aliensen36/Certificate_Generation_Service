from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin.widgets import FilteredSelectMultiple


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'last_name', 'email')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'role', 'date_issued', 'course_name',
                    'internship_start_date', 'internship_end_date')
    search_fields = ('number', 'owner',)
    list_filter = ('date_issued',)
    list_display_links = ('number', 'owner')
    readonly_fields = ('scores_display',)
    filter_horizontal = ('skills',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Навыки', is_stacked=False)},
    }

    def scores_display(self, obj):
        # Все баллы владельца сертификата
        scores = obj.scores.all()
        if not scores:
            return "Нет баллов"
        return format_html("<br>".join([f"{score.criterion}: {score.score}" for score in scores]))

    scores_display.short_description = 'Баллы владельца'


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')


class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class CriterionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('owner', 'certificate', 'criterion', 'score')
    search_fields = ('owner__name', 'owner__last_name', 'certificate__number', 'criterion__name')
    list_filter = ('criterion',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(Score, ScoreAdmin)
