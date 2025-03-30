def rank_array(scores):
    # Create a sorted list of unique scores in descending order
    unique_sorted_scores = sorted(set(scores), reverse=True)
    
    # Create a dictionary mapping scores to their ranks
    rank_dict = {}
    for rank, score in enumerate(unique_sorted_scores, 1):
        rank_dict[score] = rank
    
    # Map each score to its rank in the original order
    return [rank_dict[score] for score in scores]

# Test cases
test_cases = [
    [9, 3, 6, 10],  # Should return [2, 4, 3, 1]
    [3, 3, 3, 3, 3, 5, 1]  # Should return [2, 2, 2, 2, 2, 1, 3]
]

# Run test cases
for test in test_cases:
    result = rank_array(test)
    print(f"Input: {test}")
    print(f"Output: {result}\n") 