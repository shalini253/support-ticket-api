from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr


class TicketPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class TicketStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class TicketCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str
    priority: TicketPriority = TicketPriority.medium
    category: str = "general"
    assigned_to: str | None = None


class TicketUpdate(BaseModel):
    priority: TicketPriority | None = None
    status: TicketStatus | None = None
    assigned_to: str | None = None


class TicketResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str
    priority: str
    status: str
    category: str
    assigned_to: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True