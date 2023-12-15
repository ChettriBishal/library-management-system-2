import pytest
from unittest.mock import Mock
from src.helpers.home_menu import visitor_menu, Visitor


class TestVisitorMenu:
    @pytest.fixture
    def vis_obj(self):
        mock_visitor = Mock(spec=Visitor)
        _instance = mock_visitor.return_value
        _instance.username = 'test_user'
        return _instance

    @pytest.fixture
    def mock_get_item(self, mocker):
        return mocker.patch('src.helpers.home_menu.get_item')

    @pytest.mark.parametrize("user_inputs", [('1', 'test_name', '9')])
    def test_choice_1_none(self, user_inputs, monkeypatch, vis_obj, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))
        monkeypatch.setattr(vis_obj, 'query_book', lambda _: None)
        # vis_obj.query_book.return_value = None

        visitor_menu(vis_obj)

        captured = capsys.readouterr()
        assert captured.out.strip() == "No book with name test_name found!"

    @pytest.mark.parametrize("user_inputs", [('1', 'test_name', '9')])
    def test_choice_1_valid(self, user_inputs, monkeypatch, vis_obj, capsys, mock_get_item):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))
        monkeypatch.setattr(vis_obj, 'query_book', lambda _: True)
        mock_get_item.return_value = [3]

        visitor_menu(vis_obj)

        captured = capsys.readouterr()
        assert captured.out.strip() == "Number of copies of `test_name`: 3"

    @pytest.mark.parametrize("user_inputs", [('2', '3', '9')])
    def test_choice_2_3_sort_books(self, user_inputs, monkeypatch, vis_obj):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        vis_obj.sort_books_by_rating.return_value = True
        vis_obj.sort_books_by_price.return_value = True

        visitor_menu(vis_obj)
        vis_obj.sort_books_by_rating.assert_called() and vis_obj.sort_books_by_price.assert_called()

    @pytest.mark.parametrize("user_inputs", [('4', 'philosophy', '9')])
    def test_choice_4(self, user_inputs, vis_obj, monkeypatch):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        vis_obj.group_books_by_genre.return_value = True

        visitor_menu(vis_obj)

        vis_obj.group_books_by_genre.assert_called_once()

    @pytest.mark.parametrize("user_inputs", [('5', 'Fountainhead', '9')])
    def test_choice_5(self, user_inputs, vis_obj, monkeypatch):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        vis_obj.issue_book.return_value = True

        visitor_menu(vis_obj)

        vis_obj.issue_book.assert_called_once()

    @pytest.mark.parametrize("user_inputs", [('6', '9')])
    def test_choice_6_none(self, user_inputs, vis_obj, monkeypatch, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        vis_obj.books_issued.return_value = None

        visitor_menu(vis_obj)
        captured = capsys.readouterr()
        assert captured.out.strip() == "test_user has not issued any books yet!"

    @pytest.mark.parametrize("user_inputs", [('6', '9')])
    def test_choice_6_valid(self, user_inputs, vis_obj, monkeypatch, mocker, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        books = [('one', 'two'), ('three', 'four')]
        vis_obj.books_issued.return_value = books

        _instance = Mock()
        _instance.show_issue_details.return_value = True
        mocker.patch('src.helpers.home_menu.BookIssue', return_value=_instance)

        visitor_menu(vis_obj)

        _instance.show_issue_details.assert_called()

    @pytest.mark.parametrize("user_inputs", [('7', '9')])
    def test_choice_7(self, user_inputs, vis_obj, monkeypatch, mocker, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        books = [('one', 'two'), ('three', 'four')]

        mocker.patch('src.helpers.home_menu.get_many_items', return_value=books)

        _instance = Mock()
        _instance.show_issue_details.return_value = True
        _instance.get_dues.return_value = 101
        mocker.patch('src.helpers.home_menu.BookIssue', return_value=_instance)

        visitor_menu(vis_obj)
        capsys.readouterr()
        _instance.get_dues.assert_called()

    @pytest.mark.parametrize("user_inputs", [('8', 101, '9')])
    def test_choice_8_if(self, user_inputs, vis_obj, monkeypatch, mock_get_item, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        mock_get_item.return_value = ['test_name']
        vis_obj.return_book.return_value = True

        visitor_menu(vis_obj)
        captured = capsys.readouterr()
        assert captured.out.strip() == "Book `test_name` returned successfully!"

    @pytest.mark.parametrize("user_inputs", [('8', 101, '9')])
    def test_choice_8_else(self, user_inputs, vis_obj, monkeypatch, mock_get_item, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        mock_get_item.return_value = ['test_name']
        vis_obj.return_book.return_value = False

        visitor_menu(vis_obj)
        captured = capsys.readouterr()
        assert captured.out.strip() == "`test_user` has not issued this book!"

    @pytest.mark.parametrize("user_inputs", [('123', '9')])
    def test_choice_8_invalid(self, user_inputs, vis_obj, monkeypatch, mock_get_item, capsys):
        user_input = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        visitor_menu(vis_obj)

        captured = capsys.readouterr()

        assert captured.out.strip() == "Invalid choice!"
