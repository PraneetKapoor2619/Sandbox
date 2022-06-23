K = int(input())
room_number = list(map(int, input().split()))

compressed_room_number = set(room_number)

print(((K * sum(compressed_room_number)) - sum(room_number)) // (K - 1))