from typing import Dict , Tuple
from sqlite3 import Connectionim

class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def create_trip(self, trips_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO trips 
                (id, destination, start_data, end_datae, owner_name, owner_email)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                trips_infos["id"],
                trips_infos["destination"],
                trips_infos["start_data"],
                trips_infos["end_datae"],
                trips_infos["owner_name"],
                trips_infos["owner_email"]
            )
        )
        self.__conn.commit()
    def find_trip_by_id(self,trip_id:str):
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM trips WHERE id = ?''' ,(trip_id,)
        )
        trip = cursor.fetchone()
        return trip
    
    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE trips
                SET  status = 1
            WHERE 
                id = ?
            ''', (trip_id,)
        )
        self.__conn.commit()

