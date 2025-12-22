import os
import uuid
from datetime import datetime
from django.conf import settings


def employee_image_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    allowed_exts = getattr(settings, 'ALLOWED_IMAGE_EXTS', ['.jpg', '.png', '.jpeg'])
    if ext not in allowed_exts:
        ext = '.jpg'
    
    emp_id = getattr(instance, 'id', 'unknown')
    
    base_path = getattr(settings, 'EMPLOYEE_IMAGE_PATH', 'employee_images')
    
    now = datetime.now()
    
    return os.path.join(
        base_path,
        str(now.year),
        f"{now.month:02d}",
        f"{now.day:02d}",
        f"{emp_id}_{uuid.uuid4().hex[:8]}{ext}"
    )