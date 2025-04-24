def main():
    friends = {}
    query = None
    
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            if "<->" in line:
                person1, person2 = line.split(" <-> ")
                if person1 not in friends:
                    friends[person1] = set()
                if person2 not in friends:
                    friends[person2] = set()
                friends[person1].add(person2)
                friends[person2].add(person1)
            elif "?" in line:
                query = line.split(" ? ")
                break
        except EOFError:
            break

    if query:
        person1, person2 = query
        mutual_friends = sorted(friends.get(person1, set()) & friends.get(person2, set()))
        if mutual_friends:
            for friend in mutual_friends:
                print(friend)
        else:
            print("No mutual friend")

main()
