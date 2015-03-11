from django import forms
from django.contrib.auth.models import User
from movies.models import Movie, Actor, Character, Genre, Comment, UserProfile


class MovieForm(forms.ModelForm):

    character_list = [(c.id, c.name) for c in Character.objects.all()]

    title = forms.CharField(max_length=128, help_text="Title: ")
    year = forms.IntegerField(help_text="Year: ")
    producer = forms.CharField(max_length=128, help_text="Producer: ")
    writer = forms.CharField(max_length=128, help_text="Writer: ")
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text="Genres: "
    )

    class Meta:

        model = Movie
        fields = ('title', 'year', 'producer', 'writer', 'genres', )


class CharacterForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Name: ")
    desc = forms.Textarea()

    class Meta:

        model = Character
        fields = ('name', 'desc', )


class CommentForm(forms.ModelForm):

    comment = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ('comment', )


class UserProfileForm(forms.ModelForm):

    USER_TYPES = [(1, 'Member'), (2, 'Actor'), (3, 'Producer')]

    type = forms.ChoiceField(
        choices=USER_TYPES,
        help_text="Type: "
    )
    first_name = forms.CharField(max_length=128, help_text='First Name: ', required=False)
    last_name = forms.CharField(max_length=128, help_text='Last Name: ', required=False)

    class Meta:
        model = UserProfile
        fields = ('type', 'first_name', 'last_name', 'picture', )