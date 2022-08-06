from django.db import models


class Joke(models.Model):
    title = models.TextField(blank=True, default='')
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_title_from_content(self) -> str:
        try:
            title = self.content.split(';')[2]
            return title
        except IndexError:
            return 'knock knock joke'

    def remove_carriage_return(self) -> str:
        content = self.content.replace('/r', '')
        return content

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.content = self.remove_carriage_return()
        self.title = self.get_title_from_content()
        super(Joke, self).save(force_insert, force_update, using, update_fields)