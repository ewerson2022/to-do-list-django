from django.db import models
from django.contrib import admin

PRIORITY_CHOICES = [
    ('ALTA', 'Alta'),
    ('MEDIA', 'Média'),
    ('BAIXA', 'Baixa'),
]

class Task(models.Model):
    title = models.CharField("Título da tarefa", max_length=200)
    description = models.TextField("Descrição", blank=True, null=True)
    created_at = models.DateTimeField("data de criação", auto_now_add=True)
    completed = models.BooleanField("Concluída?", default=False)
    priority = models.CharField("Prioridade", max_length=6, choices=PRIORITY_CHOICES, default='Média')
    due_date = models.DateField("Data de vencimento", blank=True, null=True)

    def __str__(self):
        return self.title
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
