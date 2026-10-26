
import unittest
from ssd_simulator import SSDSimulator


class TestSSDSimulator(unittest.TestCase):

    def test_successful_write(self):
        ssd = SSDSimulator(total_blocks=2, max_writes=3)
        self.assertTrue(ssd.write_data("File A"))
        self.assertEqual(ssd.blocks[0]["writes"], 1)

    def test_writes_distributed(self):
        ssd = SSDSimulator(total_blocks=2, max_writes=3)
        ssd.write_data("A")
        ssd.write_data("B")
        self.assertEqual(ssd.blocks[0]["writes"], 1)
        self.assertEqual(ssd.blocks[1]["writes"], 1)

    def test_bad_block_is_skipped(self):
        ssd = SSDSimulator(total_blocks=2, max_writes=3)
        ssd.mark_block_bad(0)
        ssd.write_data("File A")
        self.assertEqual(ssd.blocks[0]["writes"], 0)
        self.assertEqual(ssd.blocks[1]["writes"], 1)

    def test_no_available_blocks(self):
        ssd = SSDSimulator(total_blocks=1, max_writes=1)
        self.assertTrue(ssd.write_data("A"))
        self.assertFalse(ssd.write_data("B"))

    def test_invalid_block_id(self):
        ssd = SSDSimulator(total_blocks=2)
        ssd.mark_block_bad(99)
        self.assertFalse(ssd.blocks[0]["bad"])
        self.assertFalse(ssd.blocks[1]["bad"])

    def test_write_limit_is_never_exceeded(self):
        ssd = SSDSimulator(total_blocks=1, max_writes=2)
        self.assertTrue(ssd.write_data("A"))
        self.assertTrue(ssd.write_data("B"))
        self.assertFalse(ssd.write_data("C"))
        self.assertEqual(ssd.blocks[0]["writes"], 2)


if __name__ == "__main__":
    unittest.main()

