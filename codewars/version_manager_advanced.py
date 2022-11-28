from typing import List, Tuple, Optional

from enum import Enum, unique

@unique
class VersionUpgrade(Enum, int):
    MAJOR = 0
    MINOR = 1
    PATCH = 2


class VersionManager:
    NUM_DIGIT_VERSION = 3
    stack: List[Tuple[int, int, int]]

    def __init__(self, version: Optional[str] = None) -> None:
        version = version or "0.0.1"
        self.stack = [self._parse_version(version)]

    @classmethod
    def _parse_version(cls, version: str) -> Tuple[int, int, int]:
        current_version = []
        version_splited = version.split(".")
        len_version_splited = len(version_splited)
        for i in range(cls.NUM_DIGIT_VERSION):
            if len_version_splited > i:
                current_version.append(cls._sanetize_number(version_splited[i]))
            else:
                current_version.append(0)
        return tuple(current_version)
    
    @staticmethod
    def _sanetize_number(number_str: str) -> int:
        numbers = ""
        for character in number_str:
            if character.isnumeric():
                numbers += character
            else:
                break
        return int(numbers) if numbers else 0

    @staticmethod
    def _upgrade_version(current_version: Tuple[int, int, int], upgrade: VersionUpgrade) -> Tuple[int, int, int]:
        next_version = []
        for i in range(len(current_version)):
            if i < upgrade:
                next_version.append(current_version[i])
            elif i == upgrade:
                next_version.append(current_version[i] + i)
            else:
                next_version.append(0)
        return tuple(next_version)

    def major(self) -> "VersionManager":
        self.stack.append(
            self._upgrade_version(self.stack[-1], VersionUpgrade.MAJOR)
        )
        return self
    
    def minor(self) -> "VersionManager":
        self.stack.append(
            self._upgrade_version(self.stack[-1], VersionUpgrade.MINOR)
        )
        return self

    def patch(self) -> "VersionManager":
        self.stack.append(
            self._upgrade_version(self.stack[-1], VersionUpgrade.PATCH)
        )
        return self
    
    def rollback(self) -> "VersionManager":
        self.stack.pop()
        return self

    def release(self) -> str:
        current_version = self.stack[-1]
        return f"{current_version[0]}.{current_version[1]}.{current_version[2]}"


