from django.shortcuts import render

# Create your views here.

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name="product_id",
                type=OpenApiTypes.NUMBER,
                location=OpenApiParameter.QUERY,
                description="Filter by product_id",
            ),
            OpenApiParameter(
                name="star_rating",
                type=OpenApiTypes.NUMBER,
                location=OpenApiParameter.QUERY,
                description="Filter by star rating",
            ),
        ],
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = self.queryset
        product_id = self.request.query_params.get("product_id")
        star_rating = self.request.query_params.get("star_rating")
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        if star_rating:
            queryset = queryset.filter(star_rating=star_rating)
        return queryset.order_by("-created_at")

    def get_serializer_class(self):
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(account_id=self.request.user.id)
