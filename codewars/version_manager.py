from typing import Optional


class Error(Exception):
    """Base class for other exceptions"""

    pass


class InvalidVersion(Error):
    """Raised when the input version is not valid"""

    pass


class NoRollback(Error):
    """Raised when is not possible to rollback"""

    pass


class VersionManager:
    def __init__(self, version: Optional[str] = "0.0.1"):
        if not version:
            version = "0.0.1"

        splited_string = version.split(".")

        major = splited_string[0]

        if len(splited_string) > 1:
            minor = splited_string[1]
            if len(splited_string) > 2:
                patch = splited_string[2]
            else:
                patch = 0
        else:
            minor = 0
            patch = 0

        try:
            self.attr_major = int(major)
            self.attr_minor = int(minor)
            self.attr_patch = int(patch)

        except ValueError:
            raise InvalidVersion("Error occured while parsing version!")

        self.previous_major = None
        self.previous_minor = None
        self.previous_patch = None

    def major(self):
        self.previous_major, self.previous_minor, self.previous_patch = (
            self.attr_major,
            self.attr_minor,
            self.attr_patch,
        )
        self.attr_major += 1
        self.attr_minor = 0
        self.attr_patch = 0

        return self

    def minor(self):
        self.previous_major, self.previous_minor, self.previous_patch = (
            self.attr_major,
            self.attr_minor,
            self.attr_patch,
        )
        self.attr_minor += 1
        self.attr_patch = 0

        return self

    def patch(self):
        self.previous_major, self.previous_minor, self.previous_patch = (
            self.attr_major,
            self.attr_minor,
            self.attr_patch,
        )
        self.attr_patch += 1

        return self

    def rollback(self):
        if self.previous_major is not None:

            self.attr_major, self.previous_major = self.previous_major, self.attr_major
            self.attr_minor, self.previous_minor = self.previous_minor, self.attr_minor
            self.attr_patch, self.previous_patch = self.previous_patch, self.attr_patch

            return self
        else:
            raise NoRollback("Cannot rollback!")

    def release(self):
        return f"{self.attr_major}.{self.attr_minor}.{self.attr_patch}"


print(VersionManager().major().rollback().release())

variable = 0
if variable:
    print("Si entro")
else:
    print("No entro")
