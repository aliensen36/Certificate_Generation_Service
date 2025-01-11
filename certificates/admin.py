from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1  # Количество пустых строк для добавления новых записей
    fields = ('criterion', 'score',)
    autocomplete_fields = ('criterion', 'owner')  # Упрощение поиска
    readonly_fields = ('owner',)  # Владелец отображается, но не редактируется

    def save_model(self, request, obj, form, change):
        """
        Автоматически назначает владельца сертификата владельцем для каждого балла.
        """
        obj.owner = obj.certificate.owner
        super().save_model(request, obj, form, change)



class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'last_name', 'email')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'role', 'date_issued', 'course_name',
                    'internship_start_date', 'internship_end_date')
    search_fields = ('number', 'owner',)
    list_filter = ('date_issued',)
    list_display_links = ('number', 'owner')
    filter_horizontal = ('skills',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Навыки', is_stacked=False)},
    }
    inlines = [ScoreInline]


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
