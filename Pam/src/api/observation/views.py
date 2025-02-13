from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.observations.models import Observation


class ObservationViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        observation = db.query(Observation).filter(Observation.eventID == pk).first()
        return Response(observation.__dict__ if observation else {})