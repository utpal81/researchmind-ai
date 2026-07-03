# Reusable schemas

from datetime import datetime
from pydantic import BaseModel


class TimestampMixin(BaseModel):
    created_at: datetime