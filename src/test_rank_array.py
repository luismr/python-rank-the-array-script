import pytest
from rank_array import rank_array

def test_basic_ranking():
    """Test basic ranking functionality"""
    scores = [9, 3, 6, 10]
    expected = [2, 4, 3, 1]
    assert rank_array(scores) == expected

def test_duplicate_scores():
    """Test handling of duplicate scores"""
    scores = [3, 3, 3, 3, 3, 5, 1]
    expected = [2, 2, 2, 2, 2, 1, 3]
    assert rank_array(scores) == expected

def test_single_score():
    """Test array with single score"""
    scores = [5]
    expected = [1]
    assert rank_array(scores) == expected

def test_empty_array():
    """Test empty array"""
    scores = []
    expected = []
    assert rank_array(scores) == expected

def test_negative_scores():
    """Test array with negative scores"""
    scores = [-5, 0, 5, -10]
    expected = [2, 3, 1, 4]
    assert rank_array(scores) == expected

def test_all_same_scores():
    """Test array with all identical scores"""
    scores = [7, 7, 7, 7, 7]
    expected = [1, 1, 1, 1, 1]
    assert rank_array(scores) == expected 