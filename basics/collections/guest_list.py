def guests_invite():
    guest_list = ["Julia", "Ivan", "Alex", "Robert", "Rosabella", "Elena", "Olga", "Ekaterina"]
    for guest in guest_list:
        print(guest, end=" ")
    print(f"\n{guest_list[-1]} will not be able to come")
    new_guest = "Maria"
    guest_list[-1] = new_guest
    print(f"Updated guest list is: ")
    for guest in guest_list:
        print(guest, end=" ")


if __name__ == "__main__":
    guests_invite()
