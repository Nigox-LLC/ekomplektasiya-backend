import logging
from django.utils import timezone
from rest_framework import status
from typing import Type, Optional
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db import transaction, IntegrityError
from rest_framework.exceptions import ValidationError


logger = logging.getLogger(__name__)


class BaseModelViewSet(ModelViewSet):
    
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    serializer_class: Type
    write_serializer_class: Optional[Type] = None
    retrieve_serializer_class: Optional[Type] = None
    
    def get_serializer_class(self) -> Type:
        if self.action == 'retrieve' and self.retrieve_serializer_class:
            return self.retrieve_serializer_class
        if self.action in ['create', 'partial_update'] and self.write_serializer_class:
            return self.write_serializer_class
        return self.serializer_class
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)
    
    @transaction.atomic
    def destroy(self, request: Request, *args, **kwargs) -> Response:
        instance = self.get_object()
        
        if not hasattr(instance, 'is_active'):
            logger.warning(
                f"{instance.__class__.__name__} modelida is_active maydoni yo'q"
            )
            raise ValidationError(
                detail={"error": "Bu model o'chirishni qo'llab-quvvatlamaydi"},
                code='soft_delete_not_supported'
            )
        
        if instance.is_active is False:
            logger.info(f"ID:{instance.pk} allaqachon o'chirilgan")
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        try:
            instance.is_active = False
            
            if hasattr(instance, 'updated_at'):
                instance.updated_at = timezone.now()
                update_fields = ['is_active', 'updated_at']
            else:
                update_fields = ['is_active']
                
            instance.save(update_fields=update_fields)
            
        except IntegrityError as e:
            logger.error(f"Database xatosi: {e}", exc_info=True)
            raise ValidationError(
                detail={"error": "Ma'lumotlar bazasi xatosi"},
                code='database_error'
            )
        
        logger.info(f"ID:{instance.pk} o'chirildi")

        return Response(status=status.HTTP_204_NO_CONTENT)