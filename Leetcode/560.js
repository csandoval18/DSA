const subarraySum = (nums, k) => {
  let count = 0
  let prefix_sum = 0
  let hm = new Map()
  hm.set(0,1)
  
  for (let i=0; i<nums.length; ++i) {
    prefix_sum = nums[i]
    // Check if remainder = prefix_sum - k  is in hm
    if (hm.has(prefix_sum - k)) 
      // Increase count by the count value of the remainder in hm since 
      // that means the number can be made up in multiple ways within the subarray
      count += hm.get(prefix_sum - k)
    // Adds new key prefix_sum with starting val 1 or adds 1 if its present
    hm.set(prefix_sum , (hm.get(prefix_sum) || 0) + 1)
  }
  return count
}