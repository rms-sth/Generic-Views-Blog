from django import forms
from .models import Post, Comment

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		# context_object_name = 'post'
# 		model = Post
# 		fields = ('title', 'content')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')