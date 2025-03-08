def get_data_from_api():
    return {"status": "success", "data": 42}

def process_data():
    data = get_data_from_api()
    return data["data"] * 2

def test_process_data(mocker):
    mocker.patch("__main__.get_data_from_api", return_value={"status": "success", "data": 10})
    assert process_data() == 20