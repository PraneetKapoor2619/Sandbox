class Message(object):

	def __init__ (self, message: str, sender: int, receiver: int) -> None:
		self.__message = message
		self.__sender = sender
		self.__receiver = receiver
	
	def __str__(self) -> str:
		return self.__message
	
	def __eq__(self, obj) -> bool:
		return self.__message == obj.__message

if __name__ == "__main__" :

	"""
	N := No. of messages
	msg1
	msg2
	...
	msgN
	E := No. of exec commands
	exec1
	exec2
	...
	exec3 
	"""
	
	import re

	Message_Obj_List = []

	for _ in range(int(input())) :
		decomposed = re.findall("^([a-zA-Z ]+) (\d+) (\d+)$", input())
		decomposed = decomposed[0]
		msg = decomposed[0]
		sender_id = decomposed[1]
		receiver_id = decomposed[2]

		Message_Obj_List.append(Message(msg, sender_id, receiver_id))

	for _ in range(int(input())) :
		command = input().split()
		if (command[0] == "eq") :
			obj_index1 = int(command[1])
			obj_index2 = int(command[2])
			result = (Message_Obj_List[obj_index1] == Message_Obj_List[obj_index2])
			print(result)
		elif (command[0] == "print") :
			obj_index = int(command[1])
			print(Message_Obj_List[obj_index])
