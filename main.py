import requests

from pprint import pprint

token = ''


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        with open('test.txt', 'rb') as f:
            href = self.get_upload_link(disk_file_path=file_path).get("href", "")
            response = requests.put(href, data=f)
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()


if __name__ == '__main__':
    uploader = YaUploader(token)
    uploader.upload('/codding/test.txt')




