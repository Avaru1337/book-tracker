def average_rating(books):
    if not books:
        return 0
    return sum(b.rating for b in books) / len(books)

def author_stats(books):
    stats = {}
    for b in books:
        author = b.author
        if author not in stats:
            stats[author] = {"count": 0, "total_rating": 0}
        stats[author]["count"] += 1
        stats[author]["total_rating"] += b.rating

    result = {}
    for author, data in stats.items():
        result[author] = {
            "books_count": data["count"],
            "avg_rating": data["total_rating"] / data["count"]
        }
    return result