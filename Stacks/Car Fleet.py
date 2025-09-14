"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
"""


"""
Input:
    - position: List[int]
    - speed: List[int]
    - target: int
Output:
    - int

Considerations:
    - Range of values for n: 1 <= n <= 1000
    - Range of values for target: 0 < target <= 1000
    - Range of values of position[i], speed[i]: 0 < speed[i] <= 100, 0 <= position[i] < target
    - All the values of position are unique.

Intuition:
    - Each car starts at a certain position behind the target, with varying speeds
    - For a single car, the time it takes to reach the detination would be (target-position[i])/speed[i]

    Example:
        - Car 1 at position 2, takes 10 hours to get to target
        - Car 2 at position 0, takes 5 hours to get to target
        - If Car 2 reaches the target BEFORE Car 1, that means at some point, it crossed Car 1, even though car 1 started 'closer' to the target
            - At the point of intersection, Car 2 SHOULD assume the speed of Car 1, and they become a single fleet

Idea:
    - Step 1:
        - Zip the position and time together for each car
        [(pos1,speed1),(pos2,speed2)..]
        - Each element would be easier to index
    
    - Step 2:
        - Sort the list, based on the positions
        - The position CLOSEST to the target should be first
        - So we would go from the car CLOEST to target, all teh way to the FURTHEST from target
    
    - Step 3:
        - For each car, calculate the TIME it takes for it to reach the target
        Example:
            - Car 1 reaches target in 10 hours
            - Car 2 reaches target in 8 hours
            - Car 3 reaches target in 6 hours
            There should only be ONE FLEET
            
            [6]

            - Car 4 reaches in 14 hours
            [6, 14]

        - If the time taken for a car that starts behind another car is LESS than the other car (Meaning it reaches before), it should be the same fleet
            - So they are jsut considered a single 'entity' that take the speed of the 'slower' car that is ahead

        - The length of the final list represents the number of car fleets
        - We want to use a STACK, because if a car that starts behind a bunch of other cars reaches the target faster, we want to pop from the stack and put in the speed of the 'slower car'
     
    Important:
        - Whenever there is an intersection, push the speed of the slower car back to the stack

    Time Complexity: O(nlogn)
    Space Complexity: O(n)
"""

def solution(position, speed, target):
    car_list = []
    stack = []

    for i in range(len(position)):
        car_list.append((position[i], speed[i]))

    # Sort the list in descending order, based on position value
    car_list.sort(reverse=True)

    for pos, sp in car_list:
        time_taken = (target - pos) / sp
        
        if stack and time_taken <= stack[-1]:
            # Not add the time taken (since it asumes the, Speed of car ahead of it)
            continue
        else:
            # Add the time_taken
            stack.append(time_taken)

    return len(stack)


pos = [4,1,0,7]
speed = [2,2,1,1]
target = 10

print(solution(pos,speed,target))