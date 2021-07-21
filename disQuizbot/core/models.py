from django.db import models
from django.utils.translation import gettext as _


class Question(models.Model):

    LEVEL = (
        (0, _('Any')),
        (1, _('Beginner')),
        (2, _('Intermidiate')),
        (3, _('Advance')),
        (4, _('Expert'))
    )

    title = models.CharField(_('title'), max_length=255)
    points = models.IntegerField(_('points'))
    difficulty = models.IntegerField(_('difficulty'), choices=LEVEL, default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)
    created_at = models.DateTimeField(
        _('created_at'), auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        _('updated_at'), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name=_(
        'Question'), on_delete=models.CASCADE)
    answer = models.CharField(_('Answer'), max_length=255)
    is_correct = models.BooleanField(_('Correct Answer'), default=False)
    is_active = models.BooleanField(_('Is Active'), default=True)
    created_at = models.DateTimeField(
        _('created_at'), auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        _('updated_at'), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.answer


class Score(models.Model):

    name = models.CharField(_("name"), max_length=255)
    points = models.IntegerField(_("points"))

    def __str__(self):
        return self.name
