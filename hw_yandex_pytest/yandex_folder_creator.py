import requests


def create_folder_yandex(folder_name, token):
    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": folder_name},
        headers={"Authorization": f"OAuth {token}"}
    )
    return response.status_code


if __name__ == '__main__':
    create_folder_yandex('hello_mister_max', 'AgAAAAAe8QLQAADLW4qBV-3QTUq2hDwiL_KJK9w')
