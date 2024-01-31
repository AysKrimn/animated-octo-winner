from django.db import models

class FormField(models.Model):
    field_name = models.CharField(max_length=100)
    display_label = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50)  # Örneğin: 'char', 'email', 'integer'
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.display_label