from enum import StrEnum


class UserRole(StrEnum):
    USER = "User"
    ADMIN = "Admin"


class CurrentAffairStatus(StrEnum):
    DRAFT = "draft"
    REVIEW = "review"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class FetchLogStatus(StrEnum):
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILED = "failed"
