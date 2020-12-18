import pytest
from yandex_folder_creator import create_folder_yandex


class TestYandexFolderCreator:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    # Проверяем создалась ли папка
    @pytest.mark.parametrize(
        'folder_name, token, response',
        # Сначала создаем папки - получаем ответ 201 все ОК
        [('Hello1', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w', 201),
         ('Hello2', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w', 201),
         ('Hello3', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w', 201),
         # Потом пробуем создать еще раз эти же папки - получаем ответ 409 - конфликт
         # (папки с таким именем уже существуют на яндекс.диске)
         ('Hello1', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w', 409),
         ('Hello2', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w', 409),
         ('Hello3', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w', 409)]
    )
    def test_create_folder_yandex(self, folder_name, token, response):
        assert create_folder_yandex(folder_name, token) == response

    def teardown_class(self):
        print('method teardown_class')
