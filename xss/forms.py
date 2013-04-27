from django import forms
from django.db.models import get_model
from blog.xss.widgets import AdvancedEditor
from blog.xss.models import Blog


class ArticleModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=AdvancedEditor())

    class Meta:
        model = Blog
