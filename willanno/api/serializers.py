from rest_framework import serializers
from willanno.core.models import InkDocument


class InkDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = InkDocument
        fields = ('id', 'author', 'authored_on', 'thumbnail', 'file')

    file = serializers.FileField(use_url=False)
