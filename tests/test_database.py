from storage.db import create_database, insert_detection, get_detections

create_database()

insert_detection("test_sign", 0.90)

data = get_detections()

if data:
    print("Database test passed!")
    print("Latest record:", data[0])
else:
    print("Database test failed!")