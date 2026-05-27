from models import Book
import storage
import stats

def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            author = input("Автор: ")
            title = input("Название: ")
            rating = input("Оценка (1-5): ")
            date = input("Дата прочтения (ГГГГ-ММ-ДД): ")
            try:
                rating = int(rating)
                if not (1 <= rating <= 5):
                    raise ValueError
            except ValueError:
                print("Ошибка: оценка должна быть целым числом от 1 до 5")
                continue
            try:
                book = Book(author, title, rating, date)
                storage.add_book(book)
                print("Книга добавлена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            books = storage.get_all_books()
            if not books:
                print("Список книг пуст.")
            for b in books:
                print(f"{b.author} - {b.title} (оценка: {b.rating}, дата: {b.date_read})")

        elif choice == "3":
            books = storage.get_all_books()
            avg = stats.average_rating(books)
            print(f"Средняя оценка: {avg:.2f}")

        elif choice == "4":
            books = storage.get_all_books()
            a_stats = stats.author_stats(books)
            if not a_stats:
                print("Нет книг для статистики.")
            for author, data in a_stats.items():
                print(f"{author}: книг - {data['books_count']}, средняя оценка - {data['avg_rating']:.2f}")

        elif choice == "5":
            author = input("Автор: ")
            title = input("Название: ")
            try:
                storage.delete_book(author, title)
                print("Книга удалена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()