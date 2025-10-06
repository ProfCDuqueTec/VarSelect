"""
Unit tests for VarSelect framework.
"""

import unittest
import numpy as np
import sys
import os

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from varselect import VarSelect


class TestVarSelect(unittest.TestCase):
    """Test cases for VarSelect class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.varselect = VarSelect()
        self.test_image = np.random.rand(100, 100)
    
    def test_initialization(self):
        """Test VarSelect initialization."""
        vs = VarSelect(variance_threshold=0.2)
        self.assertEqual(vs.variance_threshold, 0.2)
        
        # Test default initialization
        vs_default = VarSelect()
        self.assertEqual(vs_default.variance_threshold, 0.1)
    
    def test_process_valid_image(self):
        """Test processing with valid image."""
        result = self.varselect.process(self.test_image)
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, self.test_image.shape)
    
    def test_process_invalid_image(self):
        """Test processing with invalid image."""
        result = self.varselect.process(None)
        self.assertIsNone(result)
        
        empty_image = np.array([])
        result = self.varselect.process(empty_image)
        self.assertIsNone(result)
    
    def test_calculate_variance(self):
        """Test variance calculation."""
        variance_map = self.varselect.calculate_variance(self.test_image)
        self.assertEqual(variance_map.shape, self.test_image.shape)
        self.assertEqual(variance_map.dtype, np.float32)
    
    def test_selective_sobel(self):
        """Test selective Sobel filtering."""
        variance_map = np.ones_like(self.test_image)
        result = self.varselect.selective_sobel(self.test_image, variance_map)
        self.assertEqual(result.shape, self.test_image.shape)


if __name__ == '__main__':
    unittest.main()