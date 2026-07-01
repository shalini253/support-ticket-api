from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Ticket
from app.schemas import TicketCreate, TicketUpdate


def create_ticket(db: Session, ticket: TicketCreate):
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).order_by(Ticket.id).all()


def get_ticket_by_id(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


def update_ticket(db: Session, ticket_id: int, ticket_update: TicketUpdate):
    ticket = get_ticket_by_id(db, ticket_id)

    update_data = ticket_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(ticket, field, value)

    db.commit()
    db.refresh(ticket)
    return ticket


def delete_ticket(db: Session, ticket_id: int):
    ticket = get_ticket_by_id(db, ticket_id)

    db.delete(ticket)
    db.commit()

    return {"message": "Ticket deleted successfully"}