from fastapi import APIRouter
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking



router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("", response_model=list[SBooking])
async def get_bookings() -> list[SBooking]:
    bookings = await BookingDAO.find_all()
    return [SBooking.model_validate(booking) for booking in bookings]

    






