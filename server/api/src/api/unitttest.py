# 동식물 150개
import random

ChatRoomName = []

with open("/Users/isanghyeon/Developments/Dept-DISE-2020_24/2022-1-PythonProgramming-Team3/server/api/src/api/ChatroomName.txt") as f:
    FileData = f.readlines()
    for i in range(len(FileData)):
        ChatRoomName.append(FileData[i].replace("\n", ""))

while True:
    pick = random.choice(ChatRoomName)
    print(pick)
    break
