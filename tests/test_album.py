from lib.album import Album


def test_album_constructs():
    album = Album(1, "Test album", 1998, 1)
    assert album.id == 1
    assert album.title == "Test album"
    assert album.release_year == 1998
    assert album.artist_id == 1

def test_albums_format_nicely():
    album = Album(1, "Test album", 1998, 1)
    assert str(album) == "Album(1, Test album, 1998, 1)"


def test_albums_are_equal():
    album1 = Album(1, "Test album", 1998, 1)
    album2 = Album(1, "Test album", 1998, 1)
    assert album1 == album2
