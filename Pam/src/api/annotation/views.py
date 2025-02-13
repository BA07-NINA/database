from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.annotations.models import Annotation

class AnnotationViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        annotation = db.query(Annotation).filter(Annotation.annotationID == pk).first()
        return Response(annotation.__dict__ if annotation else {})