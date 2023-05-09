# function to check whether there is conflict between the time intervals of the jobs
def find_conflict(sorted_info, i):
    for j in range(i-1, -1, -1):
        if sorted_info[j][1] <= sorted_info[i][0]:
            return j
    return -1


# function to implement job scheduling with profit maximization
def profit_maximization(sorted_info, n):

    # an array to store the profit for jobs till arr[i]
    arr = [None]*n
    arr[0] = sorted_info[0][2]

    for i in range(1,n):
        profit = sorted_info[i][2]
        index = find_conflict(sorted_info, i)

        if index != -1:
            profit += arr[index]
        
        arr[i] = max(profit, arr[i-1])

    max_profit = arr[n-1]
    # print(f"The jobs which maximize the profit are : {sorted_info[1]} and {sorted_info[2]}")
    print(f"\nThe maximum profit that can be obtained is : {max_profit}")


# function to implement job scheduling with job maximization
def job_maximization(sorted_info, n):
    
    # storing the end time of the first job in sorted array
    prev_endtime = sorted_info[0][1]
    count = 1

    print(f"\nThe respective jobs which are considered in the iteration are : {sorted_info[0]}", end = " , ")
    
    for i in range(1,n):
        if sorted_info[i][0] >= prev_endtime:
            print(sorted_info[i], end = " , ")
            count += 1
            prev_endtime = sorted_info[i][1]
    
    print(f"\nThe maximum number of jobs that can be performed are : {count}\n")



# main function
if __name__ == "__main__":
    
    print("\n-----------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------")
    n = int(input("Enter the number of jobs : "))
    print("\n")

    info = []

    for i in range(n):
        values = []
        start_time = int(input(f"Enter the starting time of job {i+1} : "))
        values.append(start_time)
        end_time = int(input(f"Enter the ending time of job {i+1} : "))
        values.append(end_time)
        profit = int(input(f"Enter the profit of job {i+1} : "))
        values.append(profit)
        info.append(values)
        print("\n")

    print("-----------------------------------------------------------------------------------------------------")
    sorted_info = sorted(info, key = lambda x:x[1])
    print(f"\nThe endtime sorted list of jobs : {sorted_info}")

    print("\n-----------------------------------------------------------------------------------------------------")
    profit_maximization(sorted_info, n)
    print("\n-----------------------------------------------------------------------------------------------------")
    job_maximization(sorted_info, n)
    print("-----------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------\n")