# Unit tests for database.py


# IMPORTS
from create_database import create_database
from database import Database
from os import remove
import unittest


# main
class DatabaseTests(unittest.TestCase):
    def setUp(self):
        create_database("test_database.db")
        self.test_db = Database("test_database.db")

    def test_import_products_json(self):
        self.assertTrue(self.test_db.import_products_json("spring_products.json"))
        expected = "[1] Potatoes - 1.2 BGN - 20.0 kg\n[2] Carrots - 1.1 BGN - 6.0 kg\n[3] Cucumbers - 2.2 BGN - 3.0 kg\n[4] Lettuce - 2.1 BGN - 7.0 kg\n[5] Tomatoes - 2.7 BGN - 10.0 kg"
        self.assertEqual(expected, self.test_db.list_products())

    def test_list_products(self):
        self.test_db.import_products_json("spring_products.json")
        expected = "[1] Potatoes - 1.2 BGN - 20.0 kg\n[2] Carrots - 1.1 BGN - 6.0 kg\n[3] Cucumbers - 2.2 BGN - 3.0 kg\n[4] Lettuce - 2.1 BGN - 7.0 kg\n[5] Tomatoes - 2.7 BGN - 10.0 kg"
        self.assertEqual(expected, self.test_db.list_products())

    def test_add_product(self):
        self.assertTrue(self.test_db.add_product("Ambrosia", 20, 0.1))
        self.assertEqual("[1] Ambrosia - 20.0 BGN - 0.1 kg", self.test_db.list_products())

    def test_export_products_json(self):
        self.assertTrue(self.test_db.add_product("Ambrosia", 20, 0.1))
        self.assertEqual("[\n    {\n        \"name\": \"Ambrosia\",\n        \"price_per_kg\": 20.0,\n        \"quantity_in_kg\": 0.1\n    }\n]", self.test_db.export_products_json())

    def test_delete_product(self):
        self.assertTrue(self.test_db.add_product("Ambrosia", 20, 0.1))
        self.assertTrue(self.test_db.delete_product(1))
        self.assertEqual('', self.test_db.list_products())

    def test_update_product(self):
        self.assertTrue(self.test_db.add_product("Ambrosia", 20, 0.1))
        self.assertTrue(self.test_db.update_product("Grass", 1, 50, 1))
        self.assertEqual("[1] Grass - 1.0 BGN - 50.0 kg", self.test_db.list_products())

    def test_fetch_product_name(self):
        self.assertTrue(self.test_db.add_product("Ambrosia", 20, 0.1))
        self.assertEqual("Ambrosia", self.test_db.fetch_product_name(1))

    def test_fetch_customer_name(self):
        self.assertTrue(self.test_db.add_customer("Mityo", 15.4, 30.5))
        self.assertEqual("Mityo", self.test_db.fetch_customer_name(1))

    def test_list_customers(self):
        self.assertTrue(self.test_db.import_customers_json("spring_customers.json"))
        expected = "[1] Ivo - 5.1 kg - 17.7 BGN\n[2] Rado - 3.2 kg - 12.2 BGN"
        self.assertEqual(expected, self.test_db.list_customers())

    def test_add_customer(self):
        self.assertTrue(self.test_db.add_customer("Mityo", 15.4, 30.5))
        self.assertEqual("[1] Mityo - 15.4 kg - 30.5 BGN", self.test_db.list_customers())

    def test_delete_customer(self):
        self.assertTrue(self.test_db.add_customer("Mityo", 15.4, 30.5))
        self.assertTrue(self.test_db.delete_customer(1))
        self.assertEqual("", self.test_db.list_customers())

    def test_update_customer(self):
        self.assertTrue(self.test_db.add_customer("Mityo", 15.4, 30.5))
        self.assertTrue(self.test_db.update_customer("Mityo", 16.5, 32.1, 1))
        self.assertEqual("[1] Mityo - 16.5 kg - 32.1 BGN", self.test_db.list_customers())

    def test_export_customers_json_empty_database(self):
        self.assertEqual('[]', self.test_db.export_customers_json())

    def test_export_customers_json(self):
        self.assertTrue(self.test_db.add_customer("Mityo", 15.4, 30.5))
        expected = "{\n  []}"
        self.assertEqual(expected, self.test_db.export_customers_json())

    def tearDown(self):
        remove("test_database.db")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
