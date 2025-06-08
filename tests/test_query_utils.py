import unittest
from services.cosmos_client import get_all_contracts

class TestCosmosClient(unittest.TestCase):
    def test_get_contracts_head(self):
        contracts = get_all_contracts()
        print("contracts head 5:", contracts[:5])
        self.assertIsInstance(contracts, list)

    # paymentsも同様に
    def test_get_payments_head(self):
        from services.cosmos_client import payments_container
        payments = list(payments_container.read_all_items())
        print("payments head 5:", payments[:5])
        self.assertIsInstance(payments, list)

if __name__ == "__main__":
    unittest.main()