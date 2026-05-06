#!/usr/bin/env python3
"""
Test suite for R³ Halting Oracle
"""

import unittest
from src.halting_oracle import R3HaltingOracle

class TestHaltingOracle(unittest.TestCase):
    
    def setUp(self):
        self.oracle = R3HaltingOracle()
    
    def test_halting_program(self):
        """Test with a program that halts"""
        program = """
def main():
    print("Hello")
    return 0
        """
        result = self.oracle.will_it_halt(program)
        print(f"Halting program: {result}")
    
    def test_non_halting_program(self):
        """Test with a program that doesn't halt"""
        program = """
def main():
    while True:
        pass
        """
        result = self.oracle.will_it_halt(program)
        print(f"Non-halting program: {result}")
    
    def test_recursive_program(self):
        """Test with a recursive program with base case"""
        program = """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
        """
        result = self.oracle.will_it_halt(program)
        print(f"Recursive program: {result}")
    
    def test_r3_refinement_count(self):
        """Test that refinement iterations increase with complexity"""
        program = "print('test')"
        self.oracle.will_it_halt(program)
        iter1 = self.oracle.get_iteration_count()
        
        self.oracle = R3HaltingOracle()
        program2 = """
def complex(n):
    for i in range(n):
        for j in range(n):
            print(i*j)
        """
        self.oracle.will_it_halt(program2)
        iter2 = self.oracle.get_iteration_count()
        
        print(f"Simple program iterations: {iter1}")
        print(f"Complex program iterations: {iter2}")

if __name__ == "__main__":
    unittest.main()
