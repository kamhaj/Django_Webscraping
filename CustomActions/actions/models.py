from django.db import models

# Create your models here.

class URLContent(models.Model):
    #specify fields (primary key by default, autoincremented)
    url_address = models.CharField(max_length=300)
    encrypted_content = models.TextField()

    def __str__(self):
        return self.url_address
