class Book:
    def __init__(self, author, title, rating, date_read):
        self.author = author
        self.title = title
        self.rating = rating
        self.date_read = date_read

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["author"],
            data["title"],
            data["rating"],
            data["date_read"]
        )