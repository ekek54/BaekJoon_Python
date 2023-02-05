import heapq
def solution(book_time):
    book_time_minutes = []
    for time in book_time:
        start, end = time
        start_minute = convert_to_minute(start)
        end_minute = convert_to_minute(end)
        book_time_minutes.append((start_minute, end_minute))
    book_time_minutes.sort()
    pre_end = -1
    room = [pre_end]
    print(book_time_minutes)
    for book_time_minute in book_time_minutes:
        start, end = book_time_minute
        min_pre_end = heapq.heappop(room)
        if min_pre_end + 10 <= start:
            min_pre_end = end
        else:
            heapq.heappush(room, end)
        heapq.heappush(room, min_pre_end)
    print(room)
    return len(room)

def convert_to_minute(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute