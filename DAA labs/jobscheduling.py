#time complexity: O(nlogn)
def job_scheduling(jobs):
    max_Deadline = 0
    for i in jobs:
        if(i[1]>max_Deadline):
            max_Deadline = i[1]
    jobs.sort(key=lambda x: x[2], reverse=True)
    job_array=[-1]*max_Deadline
    total_profit=0
    for job in jobs:
        job_id=job[0]
        deadline=job[1]
        value=job[2]
        for j in range(deadline-1,-1,-1):
            if(job_array[j]==-1):
                job_array[j]=job_id
                total_profit+=value
                break
    print("Scheduling jobs:",job_array)
    print("Total profit gained:",total_profit)
jobs=[("j1",3,50),("j2",2,25),("j3",3,60),("j4",2,20),("j5",1,15)]
job_scheduling(jobs)