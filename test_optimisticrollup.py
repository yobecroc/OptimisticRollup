# test_optimisticrollup.py
"""
Tests for OptimisticRollup module.
"""

import unittest
from optimisticrollup import OptimisticRollup

class TestOptimisticRollup(unittest.TestCase):
    """Test cases for OptimisticRollup class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OptimisticRollup()
        self.assertIsInstance(instance, OptimisticRollup)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OptimisticRollup()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
