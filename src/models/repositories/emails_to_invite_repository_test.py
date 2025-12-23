import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_trip_repository = EmailsToInviteRepository(conn)

    email_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olamundo@gmail.com"
    }

    emails_to_trip_repository.registry_email(email_trips_infos)

    # Verifica se o e-mail foi inserido corretamente
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails_to_invite WHERE id = ?", (email_trips_infos["id"],))
    email_entry = cursor.fetchone()

    assert email_entry is not None
    assert email_entry[1] == trip_id
    assert email_entry[2] == "olamundo@gmail.com"
