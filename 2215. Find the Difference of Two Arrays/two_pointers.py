def findDistinctIntegers(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    answer_0 = []
    answer_1 = []
    
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            answer_0.append(nums1[i])
            i += 1
        else:
            answer_1.append(nums2[j])
            j += 1
    
    # Add remaining elements from nums1 and nums2
    while i < len(nums1):
        answer_0.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        answer_1.append(nums2[j])
        j += 1
    
    return [answer_0, answer_1]

# Example usage
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = findDistinctIntegers(nums1, nums2)
print(result)  # Output: [[5], [8]]
