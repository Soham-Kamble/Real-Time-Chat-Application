# chatapp/forms.py
from django import forms
from .models import ChatRoom

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["name"]   # slug can be auto-created
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "border rounded px-3 py-2 w-full",
                "placeholder": "Enter room name..."
            }),
        }
