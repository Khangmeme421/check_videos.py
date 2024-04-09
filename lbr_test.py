from library_item import LibraryItem
from video_library import PlayList

def test_LBR(capsys):
    test_subject= LibraryItem("Dummy Name","Dummy Director",4)

    assert "****" == test_subject.stars()
    assert "Dummy Name" == test_subject.name
    assert "Dummy Director" == test_subject.director
    assert test_subject.rating == 4


    with capsys.disabled():
        print()
        print(f"tested {test_subject.__class__.__name__} successfully")

def test_PLT(capsys):
    test_subject = PlayList("Dummy Name","Dummy Director",4,3)
    assert test_subject.key == 3
    assert test_subject.rating == 4
    assert test_subject.name == "Dummy Name"
    
    with capsys.disabled():
        print()
        print(f"tested {test_subject.__class__.__name__} successfully")
    
