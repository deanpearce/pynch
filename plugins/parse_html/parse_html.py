from bs4 import BeautifulSoup, Tag
from typing import List, Dict, Any

from core.crawldb import DbRecord

class HtmlParser:

    def __init__(self, config):
        pass

    def parse(self, doc: DbRecord) -> Dict[str, Any]:
        soup = BeautifulSoup(doc.content, 'html.parser')

        meta_tags = HtmlParser._extract_meta_tags(soup)
        title = HtmlParser._extract_title(soup)
        text = HtmlParser._extract_text(soup)
        links = HtmlParser._extract_links(soup)

        print(meta_tags)

        return {
            'meta_tags': meta_tags,
            'title': title,
            'text': text,
            'links': links,
        }

    @staticmethod
    def _extract_meta_tags(soup: BeautifulSoup) -> List[Dict[str, str]]:
        meta_tags = soup.find_all('meta')
        extracted_meta_tags = []

        for tag in meta_tags:
            attributes = tag.attrs
            extracted_meta_tags.append(attributes)

        return extracted_meta_tags

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        title_tag = soup.find('title')
        return title_tag.text if title_tag else None

    @staticmethod
    def _extract_text(soup: BeautifulSoup) -> str:
        for script in soup(['script', 'style']):
            script.decompose()

        return ' '.join(soup.stripped_strings)

    @staticmethod
    def _extract_links(soup: BeautifulSoup) -> List[str]:
        links = [a["href"] for a in soup.find_all("a", href=True)]
        return links


if __name__ == "__main__":
    html = """
    <html>
        <head>
            <title>Example Web Page</title>
            <meta charset="UTF-8">
            <meta name="description" content="Example description">
            <meta name="keywords" content="example, keywords">
        </head>
        <body>
            <h1>Welcome to the Example Web Page</h1>
            <p>This is an example web page.</p>
            <script>
                console.log("This is a script");
            </script>
            <ul>
                <li><a href="https://www.example1.com">Example 1</a></li>
                <li><a href="https://www.example2.com">Example 2</a></li>
                <li><a href="https://www.example3.com">Example 3</a></li>
            </ul>
        </body>
    </html>
    """

    parser = HtmlParser()
    result = parser.parse(html)

    print("Meta Tags:", result['meta_tags'])
    print("Title:", result['title'])
    print("Text:", result['text'])
    print("Links:", result['links'])