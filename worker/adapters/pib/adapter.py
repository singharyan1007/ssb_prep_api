from email.utils import parsedate_to_datetime
from xml.etree.ElementTree import Element

from app.api.schemas import ExtractedArticle


class PibRssAdapter:
    source_code = "PIB"

    def parse_item(self, item: Element) -> ExtractedArticle:
        publication_date = item.findtext("pubDate")

        return ExtractedArticle.model_validate(
            {
                "title": item.findtext("title", default=""),
                "source_url": item.findtext("link", default="").strip(),
                "source_code": self.source_code,
                "summary": item.findtext("description", default=""),
                "published_at": (
                    parsedate_to_datetime(publication_date.strip())
                    if publication_date and publication_date.strip()
                    else None
                ),
            }
        )


"""
Element represents one <item> from RSS XML
"""
