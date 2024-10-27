from api.models import Tutor

def test_db_connection():
    tutors = Tutor.objects.all()
    if tutors.exists():
        print("Connection successful. Found tutors:")
        for tutor in tutors:
            print(tutor.name, tutor.last_name)
    else:
        print("No tutors found or connection failed.")

test_db_connection()