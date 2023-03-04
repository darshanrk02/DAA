# function to map the proposal by a specific person to -1
def proposed_by(pref, people, proposed_to, proposed_by_):
    for j in range(len(people)-1):
        if pref[proposed_to][j][0] == proposed_by_:
            pref[proposed_to][j][1] = -1


# function to execute proposals    
def proposal(pref, people,check_proposal):
    for i in people:
      proposed_to = ""
      for j in range(len(people)-1):
          if pref[i][j][1] != 1:
              pref[i][j][1] = 1
              proposed_to = pref[i][j][0]
              break
      check_proposal.append(proposed_to)
      proposed_by(pref, people, proposed_to, i)


# function to delete elements 
def del_sym(pref, deleted, i):
    for j in pref[deleted]:
        if j[0] == i:
            pref[deleted].remove(j)


# function to remove lower priorities compared to the recieved proposals                
def remove(pref, people):
    for i in people:
        for j in range(5):
            if pref[i][-1][1] == -1:
                break
            else:
              deleted = pref[i][-1][0]
              del_sym(pref, deleted, i)
              del pref[i][-1]


# function to identify if duplicates are present in each iteration
def duplicate(second_pref):
    if len(second_pref) > len(set(second_pref)):
        return False
    else:
        return True


# function to check for cycles and remove them
def rotations(pref, people, second_pref, last_pref):
    for i in people:
        if len(pref[i]) > 1:
            last = i
            second = ""
            second_pref.append(i)
            # runs loop till no duplicates are encountered in second_pref list
            while (duplicate(second_pref)):
                second = pref[last][1][0]
                second_pref.append(second)
                last = pref[second][-1][0]
                last_pref.append(last)
            
            for i in range(len(last_pref)):
                diag1 = second_pref[i+1]
                diag2 = last_pref[i]
                del_sym(pref, diag1, diag2)
                del_sym(pref, diag2, diag1)
        
        second_pref = []
        last_pref = []



if __name__ == "__main__":
    
    print("\nconsider 'a' for Alwyn")
    print("consider 'b' for Bowie")
    print("consider 'c' for Carter")
    print("consider 'd' for David")
    print("consider 'e' for Easton")
    print("consider 'f' for Finn\n\n")

    # given preference order stored as a dictionary
    pref = {"a" : [["d",0], ["b",0], ["c",0], ["e",0], ["f",0]] , "b" : [["a",0] , ["d",0], ["c",0], ["f",0], ["e",0]] , "c" : [["b",0], ["e",0], ["f",0], ["a",0], ["d",0]] , "d" : [["e",0], ["b",0], ["c",0], ["f",0], ["a",0]] , "e" : [["f",0], ["c",0], ["d",0], ["b",0], ["a",0]] , "f" : [["c",0], ["d",0], ["e",0], ["b",0], ["a",0]]}

    # the list of people involved in the stable matching
    people = ["a", "b", "c", "d", "e", "f"]

    # list to store the people who recieved proposals
    check_proposal = []

    print("initial dictionary : \n")
    for i in people:
        print(f"{i} : {pref[i]}")
    print("\n\n")

    proposal(pref, people,check_proposal)
    
    # after proposal checking if there exists stable pair, if len(check_proposal) < len(people) indicates not all people have recieved proposal from others
    if len(check_proposal) < len(people):
        print("Stable pairs do not exist")
    
    else:
        print("preference dictionary after proposals : \n")
        for i in people:
            print(f"{i} : {pref[i]}")

        # if stable pairs exist then symmetrically delete the people who are lower in the preference than the ones proposed
        print("\n\n")
        print("preference dictionary after deletion : \n")
        remove(pref, people)
        for i in people:
            print(f"{i} : {pref[i]}")

        # if there are more than one person associated with each person we delete those by checking for cycles
        print("\n\n")
        second_pref = []
        last_pref = []
        print("preference dictionary after rotations : \n")
        rotations(pref, people, second_pref, last_pref)
        for i in people:
            print(f"{i} : {pref[i]}")

        # printing the stable pairs
        print("\n\n")
        print("There exists stable pairs")
        print("The stable pairs are : ", end = "")
        for i in people:
            print(f"( {i}, {pref[i][0][0]} )", end =' , ')
        
        print("\n\n")


    
    