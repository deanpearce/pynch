from core.injector.injector_interface import InjectorInterface

class FileInjector(InjectorInterface):

    def __init__(self, config):
        self.file_path = config['plugins']['file']['seeds'][0]

    def load_urls(self) -> str:
        urls = []
        with open(self.file_path, "r") as f:
            for line in f:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls