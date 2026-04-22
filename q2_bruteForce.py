import time
def brute_force(password):
    start_time=time.time()
    attempts=0
    length=len(password)
    max_range= 10 ** length

    for i in range(max_range):
        guess=str(i).zfill(length)
        attempts+=1
        if(guess==password):
            end_time=time.time()
            print("Guessed password: ",guess)
            print("No of attempts: ",attempts)
            print("Time taken: ",round(end_time-start_time,4))
            return
"""
pwd=input("Test password: ")
brute_force(pwd)
"""

print("Cracking 4 digit password...")
brute_force("1234")

print("\nCracking 6 digit password...")
brute_force("654321")

print("\nCracking 8 digit password...")
brute_force("87654321")
