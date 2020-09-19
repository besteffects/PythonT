def guests_invite():
    guest_list = ["Julia", "Ivan", "Alex", "Robert", "Rosabella", "Elena", "Olga", "Ekaterina"]
    for guest in guest_list:
        print(guest, end=" ")
    print(f"\n{guest_list[-1]} will not be able to come")
    new_guest = "Maria"
    guest_list[-1] = new_guest  # substituting last guest
    print(f"Updated guest list is: ")
    for guest in guest_list:
        print(guest, end=" ")
    print("A bigger dinner table was found")
    guest_list.insert(0, "Andrew")
    guest_list.insert(int(len(guest_list)/2), "Vladimir")
    guest_list.insert(-1, "Johnny")
    for guest in guest_list:
        print(f"Hi {guest}! You are invited to our dinner party!")
    print("Sorry, but only two people can be invited because of the lack of space")
    list_length = len(guest_list)
    print(f"The invitation list length is: {list_length}")
    while list_length >2:
        removed_guest = guest_list.pop()
        print(f"Dear {removed_guest}! I sincerely apologize, but you are not invited anymore ")
        list_length = list_length-1

    print(f"New invitation list length after guests removal is: {list_length}")
    for guest in guest_list:
        print(f"Dear {guest}! I am happy to announce that you are still invited to our party!")


if __name__ == "__main__":
    guests_invite()
