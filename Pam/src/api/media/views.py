from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.media.models import Media
from rest_framework import status


class MediaViewSet(viewsets.ViewSet):
    def list(self, request):
        db: Session = next(get_db())
        media = db.query(Media).all()
        return Response([m.__dict__ for m in media])

    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        media = db.query(Media).filter(Media.mediaID == pk).first()
        return Response(media.__dict__ if media else {})

    def create(self, request):
        db: Session = next(get_db())
        media = Media(**request.data)
        db.add(media)
        db.commit()
        db.refresh(media)
        return Response(media.__dict__, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        db: Session = next(get_db())
        media = db.query(Media).filter(Media.mediaID == pk).first()
        if media:
            db.delete(media)
            db.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
