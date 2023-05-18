
answer = []
dict = {}
list = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = []

for i in list:
    id_list = i.split(" ")
    if id_list[0] == "Enter":
        dict[id_list[1]] = id_list[2]
        result.append([id_list[1], '님이 들어왔습니다.'])
    elif id_list[0] == "Leave":
        result.append([id_list[1], '님이 나갔습니다.'])
    else:
        dict[id_list[1]] = id_list[2]

for i in result:
    i[0] = dict.get(i[0])
       answer.append(''.join(j for j in i))
return answer
