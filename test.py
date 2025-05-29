import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_zero(self):
        with self.assertRaises(ValueError):
            num_cols = 0
            num_rows = 0
            Maze(5, 5, num_rows, num_cols, 10, 10)

    def test_maze_create_cells_zero_columns(self):
        with self.assertRaises(ValueError):
            num_cols = 0
            num_rows = 5
            Maze(5, 5, num_rows, num_cols, 10, 10)
    
    def test_maze_create_cells_zero_rows(self):
        with self.assertRaises(ValueError):
            num_cols = 6
            num_rows = 0
            Maze(5, 5, num_rows, num_cols, 10, 10)
    
    def test_maze_create_cells_negative_columns(self):
        with self.assertRaises(ValueError):
            num_cols = -6
            num_rows = 5
            Maze(5, 5, num_rows, num_cols, 10, 10)
    
    def test_maze_create_cells_negative_rows(self):
        with self.assertRaises(ValueError):
            num_cols = 2
            num_rows = -3
            Maze(5, 5, num_rows, num_cols, 10, 10)
    


        
        
         



if __name__ == "__main__":
    unittest.main()
