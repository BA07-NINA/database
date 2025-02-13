from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from sqlalchemy.orm import Session
from session import get_db
from apps.users.models import User
from rest_framework import status

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        db: Session = next(get_db())
        users = db.query(User).all()
        return Response([u.__dict__ for u in users])

    def retrieve(self, request, pk=None):
        db: Session = next(get_db())
        user = db.query(User).filter(User.userID == pk).first()
        return Response(user.__dict__ if user else {})

    def create(self, request):
        db: Session = next(get_db())
        user = User(**request.data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return Response(user.__dict__, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        db: Session = next(get_db())
        user = db.query(User).filter(User.userID == pk).first()
        if user:
            db.delete(user)
            db.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
