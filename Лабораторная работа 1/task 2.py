# TODO Найдите количество книг, которое можно разместить на дискете
one_book_bytes = 4 * 25 * 50 * 100
volume_in_bytes = 1.44 * 1024 * 1024
print("Количество книг, помещающихся на дискету:", round((volume_in_bytes // one_book_bytes),))
