# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

# arrival(i) is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# time(i) is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.

 
from typing import List


class Solution:
  def averageWaitingTime(self, customers: List[List[int]]) -> float:
    curr_time = 0
    total_waiting_time = 0

    for arrive, time in customers:
      curr_time = max(curr_time, arrive)
      complete_time = curr_time + time
      waiting_time = complete_time - arrive
      total_waiting_time += waiting_time
      curr_time = complete_time
    
    return total_waiting_time / len(customers)