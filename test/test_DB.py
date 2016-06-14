import mock
import unittest
import sqlite3
import job_db


class MyTests(unittest.TestCase):
    @mock.patch('job_db.sqlite3.connect')
    def test_sqlDB(self, mock_sqlite3_connect):
        sqlite_execute_mock = mock.Mock()
        mock_sqlite3_connect.return_value = sqlite_execute_mock
        self.assertTrue(job_db.sqlDB("select 1"))

    def test_selectDB(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['John', 'Bob']
            self.assertEqual(job_db.selectDB("select 1", ""), ['John', 'Bob'])

    def test_connDB(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.connDB())

    def test_nProject(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.nProject('123'))

    def test_selectProject(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['John', 'Bob']
            self.assertEqual(job_db.selectProject(), ['John', 'Bob'])

    def test_sProject(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.sProject('123'))

    def test_editProject(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.editProject('123'))

    def test_lProject(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['John', 'Bob']
            self.assertEqual(job_db.lProject('123'), ['John', 'Bob'])

    def test_dProject(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.dProject('123'))

    def test_tableDB(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['John', 'Bob']
            self.assertEqual(job_db.tableDB(), ['John', 'Bob'])

    def test_delDB(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.delDB('123'))

    def test_selectCompany(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['John', 'Bob']
            self.assertEqual(job_db.selectCompany(), ['John', 'Bob'])

    def test_addPeople(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.addPeople('123'))

    def test_editPeople(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.editPeople("ДЯДЯ"))

    def test_addCompany(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.addCompany('RAMAX'))

    def test_editCompany(self):
        with mock.patch('job_db.sqlite3') as mocksql:
            self.assertTrue(job_db.editCompany("RAMAX"))

if __name__ == '__main__':
    unittest.main()