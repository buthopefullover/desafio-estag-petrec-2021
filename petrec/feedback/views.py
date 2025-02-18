from django.shortcuts import render
from .feedbacks import FeedbackForm


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'form/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'form/feedback_form.html', {'form': form})
