from typing import Dict
from sqlite3 import Connection

class TripsRepository:
    def __init__(self, conn:Connection ) -> None:
        self.__conn = conn

    def create_trip(self , trips_infos :Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute = (
            '''
                INSERT INTO trips 
                    (id , destination,  start_data, end_data ,owner_name , owner_email)
                VALUES 
                    (?,?,?,?,?,?)
            ''',(
                trips_infos["id"],
                trips_infos["destination"],
                trips_infos["start_data"],
                trips_infos["end_data"],
                trips_infos["owner_name"],
                trips_infos["owner_email"]

            )
        )
        self.__conn.commit()