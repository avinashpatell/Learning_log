from django.db import models

class Topic(models.Model):
    """A topic user is learning about"""
    text = models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    """Something Specific Learnt about the topic"""
    topic= models.ForeignKey(Topic, on_delete=models.PROTECT)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'    
    def __str__(self):
        """Return a string representation of a model"""
        if len(self.text)<=50:
            return self.text
        else:
            return self.text[:50]+'.....'