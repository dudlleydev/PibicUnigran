from django.contrib import admin
from apps.students.models import Student, Enrollment, EnrollmentSubject
from apps.students.services import add_default_subjects

# Register your models here.
class EnrollmentSubjectInline(admin.TabularInline):
    model = EnrollmentSubject
    extra = 0


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    show_change_link = True
    fields = ['curriculum_matrix', 'status']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['complete_name', 'rgm', 'email', 'phone']
    search_fields = ['complete_name', 'rgm', 'email']
    inlines = [EnrollmentInline]

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)
        if formset.model is Enrollment:
            for enrollment in formset.new_objects:
                add_default_subjects(enrollment)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'curriculum_matrix', 'status']
    list_filter = ['status', 'curriculum_matrix__course']
    search_fields = ['student__complete_name', 'student__rgm']
    autocomplete_fields = ['student']
    inlines = [EnrollmentSubjectInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        if not change:
            add_default_subjects(form.instance)


admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)