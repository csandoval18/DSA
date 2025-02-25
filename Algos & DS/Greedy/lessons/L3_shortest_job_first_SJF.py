from typing import List

'''
Geek is a software engineer. He is assigned with the task of calculating average waiting 
time of all the processes by folowwing shortest job first policy.

The shortest job first (SJF) or shortest job next, is a schedulng policy that selects 
the waiting process with the smallest execution time to execute next.

Given an array of integers bt of size n. Array bt denotes the burst time of each process.
Calculate the average waiting time of all the processes and return the nearest integer which is smaller or equal to the output.

Note: Consider all process are available at time 0.
'''

'''
1. Sort the processes based on their burst time in ascending order.

2. Calculate the waiting time for each process. The waiting time for the first process is 0,
   and for subsequent processes, it is the sum of the burst times of all previous processes.

3. Calculate the average waiting time by summing up the waiting times of all processes and 
   dividing by the number of processes.

4. Return the nearest integer that is smaller or equal to the average waiting time.
'''

class Solution:
  def solve(self, bt: List[int]):
    n = len(bt)
    bt_sorted = sorted(bt)
    
    waiting_time, total_waiting_time = 0, 0
    for i in range(n):
      total_waiting_time += waiting_time
      waiting_time += bt_sorted[i]
      
    average_waiting_time = total_waiting_time // n
    return int(average_waiting_time)

class Solution:
  def solve(self, bt: List[int]):
    bt_sorted = sorted(bt)
    t, wtime = 0, 0
    
    for i in range(len(bt)):
      wtime += t
      t += bt_sorted[i]
    return wtime // len(bt)

n = 5
bt = [4, 3, 7, 1, 2]
#     p1 p2 p3 p4 p5
#
# 0 ----- 1 ------ 3 ----- 6 ----- 10 ----- 17
#    p4       p5       p2      p1       p3

Output: 4
# Explanation: After sortinb urst times by shortest job policy