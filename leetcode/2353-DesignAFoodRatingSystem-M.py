from typing import List
import heapq
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = {}  # Maps food to its rating
        self.cuisine_heaps = defaultdict(list)  # Maps cuisine to a heap of (rating, food)
        self.food_cuisine = {}  # Maps food to its cuisine
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating[food] = rating
            self.food_cuisine[food] = cuisine
            # Use negative rating for max heap
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))
        print(self.cuisine_heaps)

    def changeRating(self, food: str, newRating: int) -> None:
        # Update the rating of the food
        self.food_rating[food] = newRating
        cuisine = self.food_cuisine[food]
        # Push the new rating into the heap
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the highest-rated food for the cuisine
        while self.cuisine_heaps[cuisine]:
            # Peek the top element of the heap
            rating, food = self.cuisine_heaps[cuisine][0]
            # Check if the rating is up to date
            if -rating == self.food_rating[food]:
                return food
            # Remove outdated ratings
            heapq.heappop(self.cuisine_heaps[cuisine])
        
# Your FoodRatings object will be instantiated and called as such:
foods, cuisines, ratings = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"], ["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]
obj = FoodRatings(foods, cuisines, ratings)
food, newRating = "sushi", 16
print(obj.changeRating(food,newRating))
cuisine = "japanese"
print(obj.highestRated(cuisine))