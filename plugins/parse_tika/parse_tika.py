from tika import parser
from typing import Optional, Dict, Any


class TikaExtractor:

    @staticmethod
    def extract_contents(file_path: str) -> Optional[Dict[str, Any]]:
        try:
            parsed_data = parser.from_file(file_path)
            return parsed_data
        except Exception as e:
            print(f"Error extracting contents from file '{file_path}': {e}")
            return None


if __name__ == "__main__":
    file_path = "plugins/parse-tika/example.pdf"  # Replace with the path to your file
    extractor = TikaExtractor()
    result = extractor.extract_contents(file_path)

    if result:
        print("Metadata:", result['metadata'])
        print("Content:", result['content'])
    else:
        print(f"Failed to extract contents from '{file_path}'")