from rest_framework import serializers
from .models import Question, Answer, Score


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'title', 'answer',
        ]


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = [
            'name',
            'points',
        ]
