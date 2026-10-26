class SSDSimulator:
    def __init__(self, total_blocks=5, max_writes=3):
        self.max_writes = max_writes
        self.blocks = [
            {"id": i, "writes": 0, "bad": False}
            for i in range(total_blocks)
        ]

    def write_data(self, data):
        available = [
            block for block in self.blocks
            if not block["bad"]
            and block["writes"] < self.max_writes
        ]

        if not available:
            print("ERROR: No healthy blocks available.")
            return False

        block = min(available, key=lambda b: b["writes"])
        block["writes"] += 1

        print(f"Write successful: {data} -> Block {block['id']}")
        return True

    def mark_block_bad(self, block_id):
        for block in self.blocks:
            if block["id"] == block_id:
                block["bad"] = True
                print(f"Block {block_id} marked as BAD.")
                return

        print("ERROR: Block does not exist.")

    def show_status(self):
        print("\nSSD BLOCK STATUS")
        for block in self.blocks:
            status = "BAD" if block["bad"] else "HEALTHY"
            print(
                f"Block {block['id']}: "
                f"Writes={block['writes']}, Status={status}"
            )


if __name__ == "__main__":
    ssd = SSDSimulator(total_blocks=3, max_writes=3)

    for i in range(9):
        ssd.write_data(f"File_{i + 1}")

    ssd.show_status()
