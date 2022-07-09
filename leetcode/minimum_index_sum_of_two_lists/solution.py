def find_restaurant(list1, list2):
    andy, doris = {}, {}
    for i in range(len(list1)):
        andy[list1[i]] = i
    for i in range(len(list2)):
        doris[list2[i]] = i

    restaurants = {}
    for restaurant in andy:
        if restaurant in doris:
            index_sum = andy[restaurant] + doris[restaurant]
            if index_sum in restaurants:
                restaurants[index_sum].append(restaurant)
            else:
                restaurants[index_sum] = [restaurant]

    return restaurants[min(list(restaurants.keys()))]


find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], [
    "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"
])
