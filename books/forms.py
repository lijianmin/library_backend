from django import forms

class AddBookForm(forms.Form):
    title = forms.CharField(label='Title of Book', max_length=200)
    author = forms.CharField(label='Author', max_length=200)
    description = forms.CharField(label='Description of Book', max_length=1000)
    summary = forms.CharField(label='Short Summary', max_length=500)
    book_cover_image_path = forms.FileField(label='Book Cover Image')    