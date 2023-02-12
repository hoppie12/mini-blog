from django.db import models


class Post(models.Model):
    '''
    данные о посте
    '''
    title = models.CharField('post title', max_length=100)
    description = models.TextField('entry text')
    author = models.CharField('Name author', max_length=100)
    data  = models.DateField('publication date')
    

    def __str__(self):
        return f'{self.title}, {self.author}'


    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Record'


