class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('user', 'rank')

