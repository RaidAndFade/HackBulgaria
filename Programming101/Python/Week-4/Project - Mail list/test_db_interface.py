# Unit tests for db_interface.py


# imports
import unittest
from db_interface import DBInterface
from create_database import create_database
from os import remove


class DbInterfaceTests(unittest.TestCase):
    def setUp(self):
        create_database("tests.db", "y")
        self.dbi = DBInterface("tests.db")
        self.maillists = [{
            "id": 1,
            "name": "Hack Bulgaria"
        }, {
            "id": 2,
            "name": "HackFMI"
        }]
        self.subscribers = [{
            "subscriber_id": 1,
            "name": "RadoRado",
            "email": "radorado@hackbulgaria.com"
        }, {
            "subscriber_id": 2,
            "name": "IvoIvo",
            "email": "ivo@hackbulgaria.com"
        }]
        self.maillists_to_subscribers = [{
            "maillist_id": 1,
            "subscriber_id": 1
        }, {
            "maillist_id": 1,
            "subscriber_id": 2
        }, {
            "maillist_id": 2,
            "subscriber_id": 2
        }, {
            "maillist_id": 2,
            "subscriber_id": 3
        }, {
            "maillist_id": 2,
            "subscriber_id": 4
        }]

    def test_fetch_maillists(self):
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())

    def test_fetch_maillist_name_by_id(self):
        self.assertEqual({"name": "Hack Bulgaria"}, self.dbi.fetch_maillist_name_by_id(1))

    def test_fetch_maillists_id_by_name(self):
        self.assertEqual({"id": 2}, self.dbi.fetch_maillists_id_by_name("HackFMI"))

    def test_create_maillist(self):
        self.assertTrue(self.dbi.create_maillist("New List"))
        new_entry = {"id": 3, "name": "New List"}
        self.maillists.append(new_entry)
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())

    def test_create_existing_maillist(self):
        self.assertTrue(not self.dbi.create_maillist("HackFMI"))
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())

    def test_update_maillist_name(self):
        self.assertTrue(self.dbi.update_maillist_name(2, "HackFMI2"))
        self.maillists[1]["name"] = "HackFMI2"
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())

    def test_update_maillist_name_to_existing_maillist_name(self):
        self.assertFalse(self.dbi.update_maillist_name(2, "Hack Bulgaria"))
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())

    def test_delete_maillist_by_id(self):
        self.assertTrue(self.dbi.delete_maillist_by_id(2))
        self.maillists.pop(1)
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())

    def test_fetch_subscribers_of_Hack_Bulgaria(self):
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))

    def test_fetch_subscriber_of_non_existing_list(self):
        self.assertEqual([], self.dbi.fetch_subscribers(3))

    def test_add_subscriber_to_Hack_Bulgaria(self):
        self.assertTrue(self.dbi.add_subscriber("Unique", "email@oscorp.com", 1))
        self.subscribers.append({"subscriber_id": 5, "name": "Unique", "email": "email@oscorp.com"})
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))

    def test_add_existing_subscriber_to_Hack_Bulgaria(self):
        self.assertFalse(self.dbi.add_subscriber("RadoRado", "radorado@hackbulgaria.com", 1))
        self.dbi.add_subscriber("RadoRado", "radorado@hackbulgaria.com", 1)
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))

    def test_update_subscriber(self):
        updated_data = {"name": "Rado", "email": "new_rado@hackbulgaria.com"}
        self.assertTrue(self.dbi.update_subscriber(1, 1, updated_data))
        self.dbi.update_subscriber(1, 1, updated_data)
        self.subscribers[0]["name"] = updated_data["name"]
        self.subscribers[0]["email"] = updated_data["email"]
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))

    def test_update_non_existing_subscriber(self):
        updated_data = {"name": "Rado", "email": "new_rado@hackbulgaria.com"}
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))
        self.dbi.update_subscriber(1, 15, updated_data)
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))

    def test_delete_subscriber(self):
        expected = [{"subscriber_id": 2, "name": "IvoIvo", "email": "ivo@hackbulgaria.com"}]
        self.assertTrue(self.dbi.delete_subscriber(1, 1))
        self.dbi.delete_subscriber(1, 1)
        self.assertEqual(expected, self.dbi.fetch_subscribers(1))

    def test_delete_non_existing_subscriber(self):
        self.dbi.delete_subscriber(1, 15)
        self.assertEqual(self.subscribers, self.dbi.fetch_subscribers(1))

    def test_fetch_maillists_by_subscriber_email(self):
        expected = [{'id': 1, 'name': 'Hack Bulgaria'}, {'id': 2, 'name': 'HackFMI'}]
        self.assertEqual(expected, self.dbi.fetch_maillists_by_subscriber_email("radorado@hackbulgaria.com"))

    def test_fetch_maillists_by_non_existing_subscriber_email(self):
        self.assertEqual([], self.dbi.fetch_maillists_by_subscriber_email("non@existing.email"))

    def test_merge_lists_HackBulgaria_HackFMI(self):
        expected = [{'email': 'radorado@hackbulgaria.com', 'name': 'RadoRado', 'subscriber_id': 1}, {'email': 'ivo@hackbulgaria.com', 'name': 'IvoIvo', 'subscriber_id': 2},
                     {'email': 'ivo@hackbulgaria.com', 'name': 'IvoIvo', 'subscriber_id': 2},
                     {'email': 'tedi@hackbulgaria.com', 'name': 'Tedi', 'subscriber_id': 3},
                     {'email': 'syndbg@hackbulgaria.com', 'name': 'Anto', 'subscriber_id': 4}]
        self.assertTrue(self.dbi.merge_lists(1, 2, "Unified List"))
        self.maillists.append({"id": 3, "name": "Unified List"})
        self.assertEqual(self.maillists, self.dbi.fetch_maillists())
        self.assertEqual(expected, self.dbi.fetch_subscribers(3))

    def tearDown(self):
        remove("tests.db")


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
