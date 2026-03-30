""" 
main entry
"""
from dogcare.dog import Dog
import dogcare.care as care

def main():
    print("🐶 Dog Care Calculator")
    print("-" * 30)
    
    species = input("Enter dog species: ")
    weight  = float(input("Enter weight (kg): "))
    size    = input("Enter size (small/medium/large): ")
    age     = float(input("Enter age (years): "))
    
    dog = Dog(species=species, weight=weight, size=size, age=age)
    
    print("\n📊 Results:")
    print(f"Human age equivalent: {care.human_years(dog)}")
    print(f"Daily water intake  : {care.water_needed(dog)}")
    print(f"Daily food intake   : {care.food_needed(dog)}")
    print(f"Walks needed        : {care.walks_needed(dog)}")
    print(care.dog_tip(dog))
        

if __name__ == "__main__":
    main()