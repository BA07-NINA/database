from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.soundQuality.models import SoundQuality

class SoundQualityViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        sound_quality = db.query(SoundQuality).filter(SoundQuality.mediaID == pk).first()
        return Response(sound_quality.__dict__ if sound_quality else {})