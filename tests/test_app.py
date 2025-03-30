from app import hello_world

def test_app_output(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello DevOps from Ubuntu!\n"
