from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.devices.models import Device

class DeviceViewSet(viewsets.ViewSet):
    def list(self, request):
        db: Session = next(get_db())
        devices = db.query(Device).all()
        return Response([d.__dict__ for d in devices])

    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        device = db.query(Device).filter(Device.deviceID == pk).first()
        return Response(device.__dict__ if device else {})