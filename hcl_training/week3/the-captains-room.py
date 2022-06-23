K = int(input())
room_number = list(map(int, input().split()))
room_number = sorted(room_number, key = room_number.count)
print(room_number[0])