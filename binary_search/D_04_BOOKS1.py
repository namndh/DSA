num_test_cases = int(input())
 
results = []
 
def check(page, num_books, books, num_subs, is_print=False):
    count = num_subs
    cur_pages = 0
    flags = [False for _ in range(501)] 
    for i in range(num_books, -1, -1):
        if books[i] > page:
            return False
        if cur_pages + books[i] > page or i < count:
            cur_pages = books[i]
            count -= 1
            flags[i] = True
            if i > 0 and count == 0:
                return False
        else:
            cur_pages += books[i]
    if is_print:
        result = ''
        for i in range(1, num_books+1):
            result += str(books[i])
            if i < num_books:
                result += ' '
            if flags[i]:
                result += ' / '
        print(result)
 
    return True
 
def run(num_books, books, num_subs):
    total_pages = sum(books)
    low = 0 
    high = total_pages
    while high - low > 1:
        mid = (high + low) // 2
        if check(mid, num_books, books, num_subs):
            high = mid
        else:
            low = mid
    check(high, num_books, books, num_subs, is_print=True)
 
for i in range(num_test_cases):
    num_books, num_subs = list(map(int, input().split(" ")))
    books = [0]
    books.extend(list(map(int, input().split(" "))))
    run(num_books, books, num_subs)