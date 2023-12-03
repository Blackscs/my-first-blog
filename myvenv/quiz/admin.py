from django.contrib import admin
from .models import Quiz, Question, Choice, QuizTaker

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Número inicial de opções exibidas na página de edição da pergunta

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3  # Número inicial de perguntas exibidas na página de edição do quiz

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuizTakerAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(QuizTaker, QuizTakerAdmin)
