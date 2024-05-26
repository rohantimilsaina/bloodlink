# views.py
from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.models import User

def chat_room(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    messages = (Message.objects.filter(sender=request.user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=request.user)).order_by('-id')
    return render(request, 'chat.html', {'receiver': receiver, 'messages': messages})

def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        receiver_id = request.POST.get('receiver_id')
        receiver = User.objects.get(id=receiver_id)
        message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('chat_room', receiver_id=receiver_id)
    else:
        return redirect('home')  # Redirect to home


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def view_users_with_messages(request):
    # Retrieve messages where the logged-in user is either sender or receiver
    messages_sent = Message.objects.filter(sender=request.user)
    messages_received = Message.objects.filter(receiver=request.user)
    
    # Extract unique users involved in these messages
    users_with_messages = set()
    for message in messages_sent:
        users_with_messages.add(message.receiver)
    for message in messages_received:
        users_with_messages.add(message.sender)
    
    # Exclude the logged-in user from the list
    users_with_messages.discard(request.user)
    
    # Pass the list of users to the template for rendering
    return render(request, 'chat_box.html', {'users_with_messages': users_with_messages})
