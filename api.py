from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from classes.openspace import Openspace
from fastapi.responses import FileResponse
import pandas as pd

# Create app
app = FastAPI()

current_openspace: Optional[Openspace] = None

@app.get("/")
def read_root():
    return {"message": "Openspace Organizer API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# Define data we expect for the initialization
class InitializeRequest(BaseModel):
    number_of_tables: int
    seats_per_table: int

class OrganizeRequest(BaseModel):
    names: List[str]


class AddColleagueRequest(BaseModel):
    name: str


class AddTableRequest(BaseModel):
    capacity: int


# New endpoitn that expects InitializeRequest
@app.post("/initialize")
def initialize_openspace(request: InitializeRequest):
    global current_openspace

    # create the openspace
    current_openspace = Openspace(request.number_of_tables, request.seats_per_table)

    return {
        "status": "succes",
        "tables": current_openspace.number_of_tables,
        "seats": current_openspace.total_capacity()
    }


@app.post("/organize")
def organize_colleagues(request: OrganizeRequest):
    global current_openspace

    if current_openspace is None:
        return {"status": "error", "message": "Please initialize openspace first"}

    success = current_openspace.organize(request.names)

    return {
        "status": "success" if success else "failed",
        "colleagues_organized": len(request.names),
    }


@app.get("/arrangement")
def get_arrangement():
    global current_openspace

    if current_openspace is None:
        return {"status": "error", "message": "Please initialize openspace first"}

    tables_info = []
    total_occupied = 0

    for i, table in enumerate(current_openspace.tables, 1):
        occupants = []
        for seat in table.seats:
            if not seat.free:
                occupants.append(seat.occupant)
                total_occupied += 1

        tables_info.append(
            {
                "table_number": i,
                "capacity": table.capacity,
                "free_spots": table.left_capacity(),
                "occupants": occupants,
            }
        )

    return {
        "tables": tables_info,
        "total_tables": current_openspace.number_of_tables,
        "total_capacity": current_openspace.total_capacity(),
        "total_occupied": total_occupied,
    }


@app.post("/add-colleague")
def add_colleague(request: AddColleagueRequest):
    global current_openspace
    if current_openspace is None:
        return {"status": "error", "message": "Initialize first"}
    success = current_openspace.add_person(request.name)
    return {
        "status": "success" if success else "failed",
        "message": f"Added {request.name}" if success else "No free seats",
        "name": request.name,
    }


@app.post("/add-table")
def add_table(request: AddTableRequest):
    global current_openspace
    if current_openspace is None:
        return {"status": "error", "message": "Initialize first"}
    current_openspace.add_table(request.capacity)
    return {
        "status": "success",
        "new_total_tables": current_openspace.number_of_tables,
        "new_total_capacity": current_openspace.total_capacity(),
    }


@app.get("/download")
def download_arrangement():
    global current_openspace
    if current_openspace is None:
        return {"status": "error", "message": "Initialize first"}

    data = {"Table": [], "Name": []}
    for table_num, table in enumerate(current_openspace.tables, 1):
        for seat in table.seats:
            if not seat.free:
                data["Table"].append(table_num)
                data["Name"].append(seat.occupant)

    filename = "seating_arrangement.xlsx"
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

    return FileResponse(
        filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="seating_arrangement.xlsx",
    )


@app.delete("/reset")
def reset_openspace():
    global current_openspace
    current_openspace = None
    return {"status": "success", "message": "Openspace has been reset"}
