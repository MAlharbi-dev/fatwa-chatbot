from django.shortcuts import render
from django.http import HttpResponse


def chatbot_view(request):
    return render(request, "chatbot/chatbot.html")


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    
    if userMessage.lower() in ['hi', 'hello', 'السلام عليكم']:
        bot_reply = "وعليكم السلام ورحمة الله وبركاته"
    else:
        bot_reply = "أنا مجرد روبوت، يرجى انتظار التحديثات!"

    return HttpResponse(bot_reply)

