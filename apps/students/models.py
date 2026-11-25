from django.db import models
from apps.courses.models import CurriculumMatrix, Subject

# Create your models here.
class Student(models.Model):
    complete_name = models.CharField(max_length=100, verbose_name='Nome Completo')
    rgm = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=19, blank=True, verbose_name='Telefone')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.complete_name

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativo'),
        ('inactive', 'Inativo'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Aluno')
    curriculum_matrix = models.ForeignKey(CurriculumMatrix, on_delete=models.PROTECT, verbose_name='Matriz Curricular')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name='Status')

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return f"{self.student.complete_name}"

class EnrollmentSubject(models.Model):
    STATUS_CHOICES = [
        ('regular', 'Regular'),
        ('credit_transfer', 'Aproveitamento'),
    ]

    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='subjects', verbose_name='Inscrição')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='Disciplina')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='regular', verbose_name='Status')
    ia_score = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='Compatibilidade (IA)')
    class Meta:
        verbose_name = 'Disciplina da Inscrição'
        verbose_name_plural = 'Disciplinas da Inscrição'
        constraints = [
            models.UniqueConstraint(fields=['enrollment', 'subject'], name='unique_enrollment_subject'),
        ]

    def __str__(self):
        return str(self.subject)
