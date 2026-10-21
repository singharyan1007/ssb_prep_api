from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, HttpUrl

class ExtractedArticle(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace = True,
        extra="forbid"
    )

    title: str = Field(min_length=1, max_length=500)
    source_url: HttpUrl
    source_code: Literal["PIB"] = "PIB"
    summary: str = Field(max_length=10000)
    published_at: AwareDatetime | None = None