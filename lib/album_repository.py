from lib.album import Album

class AlbumRepository():
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        rows = self._db_connection.execute("SELECT * FROM albums")

        albums = []

        for album_dict in rows:
            album = Album(album_dict["id"], album_dict["title"], album_dict["release_year"], album_dict["artist_id"])
            albums.append(album)
        
        return albums

    def find(self, album_id):
        rows = self._db_connection.execute("SELECT * FROM albums WHERE id = %s", [album_id])

        album = Album(rows[0]["id"], rows[0]["title"], rows[0]["release_year"], rows[0]["artist_id"])

        return album