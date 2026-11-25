from django.contrib import admin
from apps.courses.models import Course, CurriculumMatrix, Semester, Subject


# Register your models here.
class CurriculumMatrixInline(admin.TabularInline):
    model = CurriculumMatrix
    extra = 0


class SemesterInline(admin.TabularInline):
    model = Semester
    extra = 0


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
    search_fields = ['name']
    inlines = [CurriculumMatrixInline]


class CurriculumMatrixAdmin(admin.ModelAdmin):
    list_display = ['course', 'year']
    list_filter = ['course']
    search_fields = ['course__name']
    inlines = [SemesterInline]


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_number', 'curriculum_matrix']
    list_filter = ['curriculum_matrix__course']
    inlines = [SubjectInline]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'workload', 'semester']
    list_filter = ['semester__curriculum_matrix__course']
    search_fields = ['name']


admin.site.register(Course, CourseAdmin)
admin.site.register(CurriculumMatrix, CurriculumMatrixAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Subject, SubjectAdmin)