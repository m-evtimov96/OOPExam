import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):

    def setUp(self) -> None:
        self.ship = Spaceship('test', 3)

    def test_init(self):
        self.assertEqual(self.ship.name, 'test')
        self.assertEqual(self.ship.capacity, 3)
        self.assertEqual(self.ship.astronauts, [])

    def test_add_if_full(self):
        self.ship.add('astro1')
        self.ship.add('astro2')
        self.ship.add('astro3')
        with self.assertRaises(ValueError):
            self.ship.add('astro4')

    def test_add_if_already_in(self):
        self.ship.add('astro1')
        with self.assertRaises(ValueError):
            self.ship.add('astro1')

    def test_add_works(self):
        self.assertEqual(len(self.ship.astronauts), 0)
        result = self.ship.add('astro1')
        self.assertEqual(len(self.ship.astronauts), 1)
        self.assertEqual(result, 'Added astronaut astro1')
        self.assertIn('astro1', self.ship.astronauts)

    def test_remove_when_not_present(self):
        self.ship.add('astro1')
        with self.assertRaises(ValueError):
            self.ship.remove('astro2')

    def test_remove_works(self):
        self.assertEqual(len(self.ship.astronauts), 0)
        self.ship.add('astro1')
        self.assertEqual(len(self.ship.astronauts), 1)
        self.assertIn('astro1', self.ship.astronauts)
        result = self.ship.remove('astro1')
        self.assertEqual(len(self.ship.astronauts), 0)
        self.assertNotIn('astro1', self.ship.astronauts)
        self.assertEqual(result, 'Removed astro1')


if __name__ == '__main__':
    unittest.main()