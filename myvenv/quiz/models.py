from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título do Quiz')
    description = models.TextField(verbose_name='Descrição do Quiz')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name='Quiz Relacionado')
    text = models.TextField(verbose_name='Texto da Pergunta')

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', verbose_name='Pergunta Relacionada')
    text = models.CharField(max_length=255, verbose_name='Texto da Opção')
    is_correct = models.BooleanField(default=False, verbose_name='Correta')

    def __str__(self):
        return self.text

class QuizTaker(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_takers', verbose_name='Quiz Relacionado')
    user = models.CharField(max_length=255, verbose_name='Usuário')
    score = models.IntegerField(default=0, verbose_name='Pontuação')

    def __str__(self):
        return f'{self.user} - {self.quiz.title}'
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título do Quiz')
    description = models.TextField(verbose_name='Descrição do Quiz')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name='Quiz Relacionado')
    text = models.TextField(verbose_name='Texto da Pergunta')

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', verbose_name='Pergunta Relacionada')
    text = models.CharField(max_length=255, verbose_name='Texto da Opção')
    is_correct = models.BooleanField(default=False, verbose_name='Correta')

    def __str__(self):
        return self.text

class QuizTaker(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_takers', verbose_name='Quiz Relacionado')
    user = models.CharField(max_length=255, verbose_name='Usuário')
    score = models.IntegerField(default=0, verbose_name='Pontuação')

    def __str__(self):
        return f'{self.user} - {self.quiz.title}'
