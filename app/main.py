from fastapi import FastAPI, Query, Depends
from typing import Union
from datetime import date

from app.bookings.router import router as router_bookings


app = FastAPI()

app.include_router(router_bookings)


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: bool = False,
        stars: Union[int, None] = Query(None, ge=1, le=5),
    ):
        self.location = location 
        self.date_from = date_from 
        self.date_to = date_to 
        self.has_spa = has_spa 
        self.stars = stars 


@app.get("/hotels/")
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


@app.post("/bookings")
def add_booking():
    ...