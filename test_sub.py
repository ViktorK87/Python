import pytest
from sqlalchemy import create_engine
from sub_page import SubjectPage


db_connection_string = "postgresql://postgres:1987@localhost:5432/postgres"
db = create_engine(db_connection_string)


@pytest.fixture
def db_connection():
    connection = db.connect()
    transaction = connection.begin()
    yield connection, transaction
    transaction.rollback()
    connection.close()


def test_crud_subject(db_connection):
    connection, transaction = db_connection
    subject_page = SubjectPage(connection)

    count_before = subject_page.count_subjects()
    subject_page.insert_subject("Applied Math II")
    count_after = subject_page.count_subjects()

    assert count_after == count_before + 1

    result = subject_page.get_subject("Applied Math II")
    assert result.fetchone() is not None

    subject_page.delete_subject("Applied Math II")
    result = subject_page.get_subject("Applied Math II")
    assert result.fetchone() is None
