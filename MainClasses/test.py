from MainClasses.MouseAndKeyboard import mouse_actions

mouse = mouse_actions.Mouse()

import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a = mouse
    def test_something(self):
        self.te

if __name__ == '__main__':
    unittest.main()
