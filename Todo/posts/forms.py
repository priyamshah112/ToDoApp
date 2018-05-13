from django import forms

status_choices =('Not-Started','In-Progress','Done')
class PostForm(forms.Form):
	title = forms.CharField(max_length=50,widget=forms.TextInput(
		attrs ={'class' : 'form-control' , 'id' : 'title'}))
	description = forms.CharField(
		        max_length=2000,
        widget=forms.Textarea(attrs ={'class' : 'form-control' ,'rows' : '5', 'id' : 'description'}))
	status = forms.CharField(max_length=50,widget=forms.TextInput(
		attrs ={'class' : 'form-control' , 'id' : 'status'}))
