from django.shortcuts import render

QUIZ = {
    1: {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris",
    },
    2: {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4",
    },
    3: {
        "question": "What is the capital of Germany?",
        "options": ["Berlin", "Madrid", "Rome", "Lisbon"],
        "answer": "Berlin",
    },
}


def quiz_view(request):
    if request.method == "POST":
        score = 0
        total = len(QUIZ)
        for q_id, q_data in QUIZ.items():
            selected = request.POST.get(str(q_id))
            if selected == q_data["answer"]:
                score += 1
        return render(request, "quiz/result.html", {"score": score, "total": total})

    return render(request, "quiz/quiz.html", {"quiz": QUIZ})
