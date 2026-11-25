from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Curso')
    duration = models.IntegerField(blank=True, null=True, verbose_name='Duração do Curso (em anos)')
    coordinators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name='Coordenadores')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name

class CurriculumMatrix(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    year = models.IntegerField(verbose_name='Ano')
    
    class Meta:
        verbose_name = 'Matriz Curricular'
        verbose_name_plural = 'Matrizes Curriculares'
    
    def __str__(self):
        return f"{self.course.name} - {self.year}"

class Semester(models.Model):
    curriculum_matrix = models.ForeignKey(CurriculumMatrix, on_delete=models.CASCADE, verbose_name='Matriz Curricular')
    semester_number = models.IntegerField(verbose_name='Número do Semestre')
    
    class Meta:
        verbose_name = 'Semestre'
        verbose_name_plural = 'Semestres'

    def __str__(self):
        return f"{self.curriculum_matrix} - {self.semester_number}º semestre"

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name='Semestre')
    name = models.CharField(max_length=50, verbose_name='Nome da Disciplina')
    workload = models.IntegerField(verbose_name='Carga Horária')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        
    def __str__(self):
        return self.name