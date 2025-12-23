from rest_framework.exceptions import APIException


class AnnualPlanValidationError(APIException):
    """Annual plan bo'yicha custom validation xatoligi."""
    status_code = 400
    default_detail = "AnnuYillikal plan validatsiya xatoligi."
    default_code = "annual_plan_validation_error"


class AnnualPlanCreationError(APIException):
    """Annual plan yaratishdagi xatolik."""
    status_code = 500
    default_detail = "Yillik plan yaratishda xatolik yuz berdi."
    default_code = "annual_plan_creation_error"