import pytest
import unittest
from secretaty_programm import remove_doc_from_shelf, get_all_doc_owners_names, check_document_existance, \
    add_new_shelf, append_doc_to_shelf, get_doc_owner_name, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_all_docs_info, add_new_doc


class TestSomething:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    # Проверка документов по номеру
    @pytest.mark.parametrize('doc_number, result', [('2207 876234', True), ('11-2', True), ('5455 028765', False),
                                                    ('01', False), ('10006', True)])
    def test_check_document_existance(self, doc_number, result):
        assert check_document_existance(doc_number) == result

    # Поиск имени по документу
    @pytest.mark.parametrize('doc_number, result',
                             [('2207 876234', 'Василий Гупкин'), ('11-2', 'Геннадий Покемонов'),
                              ('10006', 'Аристарх Павлов'), ('007', False)])
    def test_get_doc_owner_name(self, doc_number, result):
        assert get_doc_owner_name(doc_number) == result

    # Список владельцев документов
    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}

    # Удаление документа с полки
    @pytest.mark.parametrize('doc_number, result', [('2207 876234', True), ('11-2', True), ('5455 028765', True),
                                                    ('01', False)])
    def test_remove_doc_from_shelf(self, doc_number, result):
        assert remove_doc_from_shelf(doc_number) == result

    # Добавление новой полки
    @pytest.mark.parametrize('shelf_number, result', [('1', False), ('2', False), ('3', False), ('4', True)])
    def test_add_new_shelf(self, shelf_number, result):
        assert add_new_shelf(shelf_number) == result

    # Добавление документа на полку
    @pytest.mark.parametrize('doc_number, shelf_number, result',
                             [('10006', '2', True), ('2207 876234', '1', True),
                              ('11-2', '1', True), ('5455 028765', '1', True), ('007', '3', True),
                              ('007-12-14', '4', True), ('199', '1', True)])
    def test_append_doc_to_shelf(self, doc_number, shelf_number, result):
        assert append_doc_to_shelf(doc_number, shelf_number) == result

    # Удаление документа
    @pytest.mark.parametrize('user_doc_number, result', [('1', False), ('2', False), ('3', False), ('4', False),
                                                         ('2207 876234', True), ('11-2', True)])
    def test_delete_doc(self, user_doc_number, result):
        assert delete_doc(user_doc_number) == result

    # Поиск полки по номеру документа
    @pytest.mark.parametrize('user_doc_number, result', [('10006', True), ('0', False)])
    def test_get_doc_shelf(self, user_doc_number, result):
        assert get_doc_shelf(user_doc_number) == result

    # Перемещение документа на полку(если полки нет то создается новая, текущая позиция документа удаляется)
    @pytest.mark.parametrize('user_doc_number, user_shelf_number, result', [('1', '2', True), ('6', '11-2', True)])
    def test_move_doc_to_shelf(self, user_doc_number, user_shelf_number, result):
        assert move_doc_to_shelf(user_doc_number, user_shelf_number) == result

    # Показать список всех документов
    def test_show_all_docs_info(self):
        assert show_all_docs_info() == True

    # Добавление нового документа
    @pytest.mark.parametrize('new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, result',
                             [('007', 'больничный', 'Геннадий Букин', '4', ('4', True)),
                              ('439 733', 'passport', 'Лунтин', '113', ('113', True)),
                              ('03-11-12', 'военник', 'Служилов Артем', '2', ('2', True)),
                              ('12АБВ', 'водительское удостоверение', 'Валентин Таксович', '3', ('3', True))])
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, result):
        assert add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number) == result

    def teardown_class(self):
        print('method teardown_class')


