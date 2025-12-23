import uuid
from datetime import datetime, timedelta
import pytest
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())
@pytest.fixture
def trips_repo():
    conn = db_connection_handler.get_connection()
    return TripsRepository(conn)

def test_create_trip(trips_repo):
    trips_infos = {
        "id": trip_id,
        "destination": "Holanda",
        "start_data": datetime.strptime("26-12-2025", "%d-%m-%Y"),
        "end_datae": datetime.strptime("26-12-2025", "%d-%m-%Y") + timedelta(days=13),
        "owner_name": "Gabriel",
        "owner_email": "paivinha69@gmail.com"
    }

    
    trips_repo.create_trip(trips_infos)

    #
    conn = db_connection_handler.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trips WHERE id = ?", (trips_infos["id"],))
    trip = cursor.fetchone()

    assert trip is not None
    assert trip[1] == trips_infos["destination"]  
    assert trip[4] == trips_infos["owner_name"]   


def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id)
    print()
    print(trip)

def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.update_trip_status(trip_id)