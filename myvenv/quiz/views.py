from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Choice, QuizTaker

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        # Processar as respostas submetidas pelo usuário
        user_choices = request.POST.getlist('choice')
        score = calculate_score(questions, user_choices)

        # Registrar a pontuação do usuário
        QuizTaker.objects.create(quiz=quiz, user=request.user.username, score=score)

        return render(request, 'quiz/quiz_result.html', {'score': score})

    return render(request, 'quiz/quiz_view.html', {'quiz': quiz, 'questions': questions})

def calculate_score(questions, user_choices):
    # Calcular a pontuação com base nas respostas do usuário
    score = 0
    for question_id, user_choice_id in zip(questions, user_choices):
        question = Question.objects.get(id=question_id)
        correct_choice = question.choices.get(is_correct=True)
        if int(user_choice_id) == correct_choice.id:
            score += 1
    return score
