def world_locations_sort():
    world_places = ["Zanzibar", "Nairobi", "Melbourne", "Toronto", "Niagara Falls", "Milan", "Juneau"]
    print(world_places)
    #  Printing without modifying an original list
    print(sorted(world_places))
    #  Verify actual list sorting order did not change
    print(world_places)
    world_places.reverse()
    print(f"Reversed list order: {world_places}")
    world_places.reverse()
    print(f"The list after it was reversed back: {world_places}")
    world_places.sort()
    print(f"Sorted list with sort(){world_places}")
    world_places.sort(reverse=True)
    print(f"List sorted in reverse alphabetical order{world_places}")


if __name__ == "__main__":
    world_locations_sort()
