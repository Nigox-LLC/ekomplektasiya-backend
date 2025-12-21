from django.db import models
from django.utils import timezone
from typing import Any, Optional, TypeVar

T = TypeVar('T', bound='BaseModel')


class ActiveQuerySet(models.QuerySet[T]):
    def active(self) -> models.QuerySet[T]:
        return self.filter(is_active=True)
    
    def inactive(self) -> models.QuerySet[T]:
        return self.filter(is_active=False)
    
    def delete(self, hard: bool = False) -> tuple[int, dict[str, int]] | int:
        if hard:
            return super().delete()
        
        return self.update(is_active=False, updated_at=timezone.now())
    

class ActiveManager(models.Manager[T]):
    
    def get_queryset(self) -> ActiveQuerySet[T]:
        return ActiveQuerySet(self.model, using=self._db).active()
    
    def all_with_inactive(self) -> ActiveQuerySet[T]:
        return ActiveQuerySet(self.model, using=self._db)


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,db_index=True
    )
    is_active = models.BooleanField(
        default=True,
    )
    
    objects = models.Manager()
    
    active = ActiveManager()
    
    class Meta:
        abstract = True
        
        ordering = ['-created_at']
        
        indexes = [
            models.Index(
                fields=['-created_at'],
                name='%(app_label)s_%(class)s_created_idx'
            ),
            models.Index(
                fields=['-updated_at'],
                name='%(app_label)s_%(class)s_updated_idx'
            ),
        ]
        
        default_permissions = ('add', 'change', 'delete', 'view')
        
        base_manager_name = 'objects'
    
    def __str__(self) -> str:
        return f"{self._meta.verbose_name.title()} #{self.pk}"
    
    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.pk}, active={self.is_active}, "
            f"created={self.created_at.isoformat() if self.created_at else None})>"
        )
    
    def delete(self, hard: bool = False, *args: Any, **kwargs: Any) -> Optional[tuple[int, dict[str, int]]]:
        if hard:
            return super().delete(*args, **kwargs)
        self.is_active = False
        self.save(update_fields=['is_active', 'updated_at'])
        return None
    
    def hard_delete(self, *args: Any, **kwargs: Any) -> tuple[int, dict[str, int]]:
        return super().delete(*args, **kwargs)

    
   