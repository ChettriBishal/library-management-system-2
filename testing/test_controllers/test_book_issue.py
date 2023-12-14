import pytest
from unittest.mock import patch
from src.controllers.book_issue import BookIssue, datetime


class TestBookIssue:
    @pytest.fixture
    def book_issue_obj(self):
        obj = BookIssue(101, 'test_user', 90, '2023-10-30', '2023-12-01', 0)
        return obj

    def test_get_details(self, book_issue_obj):
        res = book_issue_obj.get_issue_details
        assert res is not None

    def test_show_issue_details(self, monkeypatch, book_issue_obj):
        monkeypatch.setattr('builtins.print', lambda _: True)
        res = book_issue_obj.show_issue_details()
        assert res is None

    @patch('src.controllers.book_issue.insert_item')
    def test_add_book(self, mock_insert_item, capsys, book_issue_obj):
        mock_insert_item.return_value = True

        book_issue_obj.add_book('test_book')
        captured = capsys.readouterr()
        assert captured.out.strip() == "test_book is successfully issued!!"

    def test_get_dues(self, book_issue_obj):
        val = book_issue_obj.get_dues()
        assert val > 0
