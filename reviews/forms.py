from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Your Name", max_length=10, error_messages={
#     "required": "you are fucking stupid" ,
#     "max_length": "who has name above 10 characters you are a legend!!" 
#   })
#   review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#   rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ["user_name", "review_text", "rating"]
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
          "user_name": "Your Name",
          "review_text": "Your Review",
          "rating": "Your Rating"
        }
        error_messages = {
          "user_name": {
            "required": "you are fucking stupid" ,
            "max_length": "who has name above 10 characters you are a legend!!" 
          }
        }
