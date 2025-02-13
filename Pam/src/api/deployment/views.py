from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.deployments.models import Deployment
from rest_framework import status

class DeploymentViewSet(viewsets.ViewSet):
    def list(self, request):
        db: Session = next(get_db())
        deployments = db.query(Deployment).all()
        return Response([d.__dict__ for d in deployments])

    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        deployment = db.query(Deployment).filter(Deployment.deploymentID == pk).first()
        return Response(deployment.__dict__ if deployment else {})

    def create(self, request):
        db: Session = next(get_db())
        deployment = Deployment(**request.data)
        db.add(deployment)
        db.commit()
        db.refresh(deployment)
        return Response(deployment.__dict__, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        db: Session = next(get_db())
        deployment = db.query(Deployment).filter(Deployment.deploymentID == pk).first()
        if deployment:
            db.delete(deployment)
            db.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)