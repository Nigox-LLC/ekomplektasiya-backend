import logging
from typing import Dict, List, Any, Optional
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404

from .exceptions import AnnualPlanValidationError, AnnualPlanCreationError
from apps.documents.plan.models import AnnualPlan, AnnualPlanItem, AnnualPlanItemMonth


logger = logging.getLogger(__name__)


class AnnualPlanService:

    @classmethod
    @transaction.atomic
    def save_annual_plan(cls, validated_data: Dict[str, Any]) -> AnnualPlan:
       
        items_data: List[Dict[str, Any]] = validated_data.pop('items', [])
        plan_id: Optional[int] = validated_data.pop('id', None)
        
        try:
            if plan_id:
                logger.info(f"AnnualPlan yangilanmoqda: ID={plan_id}")
                annual_plan = cls._update_plan(plan_id, validated_data, items_data)
                logger.info(f"AnnualPlan yangilandi: ID={annual_plan.id}, {len(items_data)} ta element")
            else:
                logger.info("Yangi AnnualPlan yaratilmoqda...")
                annual_plan = cls._create_plan(validated_data, items_data)
                logger.info(f"Yangi AnnualPlan yaratildi: ID={annual_plan.id}, {len(items_data)} ta element")
                
            return annual_plan
            
        except AnnualPlan.DoesNotExist:
            logger.error(f"AnnualPlan topilmadi: ID={plan_id}")
            raise AnnualPlanValidationError(detail=f"ID={plan_id} bo'lgan plan topilmadi.")
        except IntegrityError as e:
            logger.error(f"Database xatoligi: {str(e)}", exc_info=True)
            raise AnnualPlanCreationError(detail="Ma'lumotlar bazasi integratsiya xatoligi yuz berdi.")
        except Exception as e:
            logger.error(f"AnnualPlan saqlashda xatolik: {str(e)}", exc_info=True)
            raise AnnualPlanCreationError(detail=f"Kutilmagan xatolik: {str(e)}")

    @staticmethod
    def _create_plan(plan_data: Dict[str, Any], items_data: List[Dict[str, Any]]) -> AnnualPlan:
        annual_plan = AnnualPlan.objects.create(**plan_data)
        AnnualPlanService._process_items(annual_plan, items_data)
        return annual_plan

    @staticmethod
    def _update_plan(
        plan_id: int, 
        plan_data: Dict[str, Any], 
        items_data: List[Dict[str, Any]]
    ) -> AnnualPlan:

        annual_plan = get_object_or_404(AnnualPlan, id=plan_id)
        
        immutable_fields = ['region', 'for_year', 'district']
        for field in immutable_fields:
            if field in plan_data:
                raise AnnualPlanValidationError(
                    detail=f"Maydon '{field}' ni o'zgartirish mumkin emas. "
                           f"Bu kalit maydonlar update qilinmaydi."
                )
        
        updateable_fields = ['comment', 'status', 'description']
        updated_fields = []
        
        for field in updateable_fields:
            if field in plan_data:
                setattr(annual_plan, field, plan_data[field])
                updated_fields.append(field)
        
        if updated_fields:
            annual_plan.save(update_fields=updated_fields)
            logger.debug(f"AnnualPlan maydonlari yangilandi: {updated_fields}")
        
        
        AnnualPlanService._process_items(annual_plan, items_data)
        
        return annual_plan

    @staticmethod
    def _process_items(annual_plan: AnnualPlan, items_data: List[Dict[str, Any]]) -> None:
       
        if not items_data:
            logger.warning(f"Itemlar ro'yhati bo'sh. Plan ID={annual_plan.id}")
            return
        
        month_objects_to_create = []
        created_items_count = 0
        
        for item_index, item_data in enumerate(items_data, 1):
            months_data = item_data.pop('months', [])
            
            plan_item = AnnualPlanItem.objects.create(
                annual_plan=annual_plan,
                **item_data
            )
            created_items_count += 1
            
            for month_data in months_data:
                month_obj = AnnualPlanItemMonth(
                    item=plan_item,
                    **month_data
                )
                month_objects_to_create.append(month_obj)
            
            if item_index % 50 == 0:
                logger.debug(f"{item_index} ta plan elementi yaratildi...")
        
        if month_objects_to_create:
            try:
                AnnualPlanItemMonth.objects.bulk_create(month_objects_to_create)
                logger.info(
                    f"Barcha oylar yaratildi: {len(month_objects_to_create)} ta obyekt, "
                    f"{created_items_count} ta item uchun"
                )
            except Exception as e:
                logger.error(f"Bulk create xatoligi: {str(e)}", exc_info=True)
                raise AnnualPlanValidationError(detail="Oylar yaratishda xatolik yuz berdi.")
        
        logger.info(f"Nested itemlar muvaffaqiyatli yaratildi: {created_items_count} ta item")