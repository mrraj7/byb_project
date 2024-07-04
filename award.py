# =============== Auto-graded Task 3 ================
# This program determines the award a person competing in a triathlon (swimming, cycling, and running)
swimming_timings = int(input("Enter the swimming timings in minutes : "))
cycling_timings = int(input("Enter the cycling timings in minutes : "))
running_timings = int(input("Enter the running timings in minutes : "))
total_time = swimming_timings + cycling_timings + running_timings
# Determine award based on the total time taken
if total_time <= 100:
    print("Provincial colours")
elif total_time <= 105:
    print("Provincial half colours")
elif total_time <= 110:
    print("Provincial scroll")
elif total_time >= 111:
    print("No award")
