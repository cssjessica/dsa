from sortedcontainers import SortedSet

class FoodRatings:

    # O(n logn)
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_food = defaultdict(SortedSet) # cuisine -> (rating, food)
        self.cuisines = {} # food -> cuisine
        self.ratings = {} # food -> rating

        for i in range(len(foods)):
            self.cuisines_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    # O(log n)
    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisines[food]
        r = self.ratings[food]

        self.cuisines_food[c].remove((-r, food))
        self.cuisines_food[c].add((-newRating, food))

        self.ratings[food] = newRating
        
    # O(1)
    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_food[cuisine][0][1]        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
