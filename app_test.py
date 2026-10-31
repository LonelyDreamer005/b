from app import app
c = app.test_client()

def test_home():
    r = c.get('/')
    assert r.status_code == 200

def test_get_students():
    res = c.get("/student")
    assert res.status_code == 200


def test_add_student():
    res = c.post("/student", json={"name": "Alice", "course": "CS"})
    assert res.status_code == 201