#
# InkDocument
#   list
#   (bulk) import
#
# Annotation
#   list
#   create
#   update
#
import datetime
from rest_framework import viewsets, views, parsers
from rest_framework.response import Response
from willanno.core.models import InkDocument, InkDocumentAnnotation
from willanno.api.serializers import InkDocumentSerializer


class InkDocumentViewSet(viewsets.ModelViewSet):
    queryset = InkDocument.objects.all()
    serializer_class = InkDocumentSerializer


class InkDocumentView(views.APIView):
    parser_classes = (parsers.MultiPartParser,)

    def get(self, request, **kwargs):
        document_id = kwargs.get('id')

        # Return the binary file related to the specified document
        if document_id:
            document = InkDocument.objects.get(id=document_id)
            with open(document.file.path, 'r') as fp:
                file_data = fp.read()
            return Response(file_data, content_type='application/octet-stream')

        # Return a list of all documents
        else:
            documents = InkDocument.objects.all()
            data = InkDocumentSerializer(documents, many=True).data
            return Response(data)

    def post(self, request):
        document = InkDocument(author='Vix', authored_on=datetime.datetime.now(), file=request.FILES['file'])
        document.save()
        return Response(status=204)

    def put(self, request, **kwargs):
        document_id = kwargs.get('id')
        if not document_id:
            return Response('Document id not supplied', status=400)

        annotation = InkDocumentAnnotation(ink_document_id=document_id, file=request.FILES['file'])
        annotation.save()

        return Response(status=204)


class InkDocumentAnnotationView(views.APIView):
    def get(self, request, **kwargs):
        document_id = kwargs.get('id')
        if document_id:
            document = InkDocumentAnnotation.objects.get(ink_document__id=document_id)
            with open(document.file.path, 'r') as fp:
                file_data = fp.read()
            # return Response(file_data, content_type='text/plain')
            return Response(file_data)

