from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin.widgets import FilteredSelectMultiple


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'last_name', 'email')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'date_issued')
    search_fields = ('number', 'owner__email')
    list_filter = ('number', 'owner__email', 'date_issued',)
    list_display_links = ('number', 'owner')
    readonly_fields = ('scores_display',)
    filter_horizontal = ('skills',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Навыки', is_stacked=False)},
    }

    # Поиск по номеру сертификата или email владельца
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct

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
    list_display = ('owner', 'criterion', 'score')
    search_fields = ('owner__name', 'owner__last_name', 'criterion__name')
    list_filter = ('owner__name', 'owner__last_name', 'criterion__name')


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(Score, ScoreAdmin)
