from typing import List
from typing import Optional
from typing import Tuple


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

    def major(self) -> "VersionManager":
        current_version = self.stack[-1]
        self.stack.append((current_version[0] + 1, 0, 0))
        return self

    def minor(self) -> "VersionManager":
        current_version = self.stack[-1]
        self.stack.append((current_version[0], current_version[1] + 1, 0))
        return self

    def patch(self) -> "VersionManager":
        current_version = self.stack[-1]
        self.stack.append((current_version[0], current_version[1], current_version[2] + 1))
        return self

    def rollback(self) -> "VersionManager":
        self.stack.pop()
        return self

    def release(self) -> str:
        current_version = self.stack[-1]
        return f"{current_version[0]}.{current_version[1]}.{current_version[2]}"


print(VersionManager().release())
print(VersionManager("").release())
print(VersionManager("1.2.3").release())
print(VersionManager("1.2.3.4").release())
print(VersionManager("1.2.3.d").release())
print(VersionManager("1").release())
print(VersionManager("1.1").release())

"""
@test.describe("Sample tests")
def sample_tests():


    @test.it("Major releases tests")
    def it_2():
        test.assert_equals(VersionManager().major().release(), "1.0.0")
        test.assert_equals(VersionManager("1.2.3").major().release(), "2.0.0")
        test.assert_equals(VersionManager("1.2.3").major().major().release(), "3.0.0")

    @test.it("Minor releases tests")
    def it_3():
        test.assert_equals(VersionManager().minor().release(), "0.1.0")
        test.assert_equals(VersionManager("1.2.3").minor().release(), "1.3.0")
        test.assert_equals(VersionManager("1").minor().release(), "1.1.0")
        test.assert_equals(VersionManager("4").minor().minor().release(), "4.2.0")

    @test.it("Patch releases tests")
    def it_4():
        test.assert_equals(VersionManager().patch().release(), "0.0.2")
        test.assert_equals(VersionManager("1.2.3").patch().release(), "1.2.4")
        test.assert_equals(VersionManager("4").patch().patch().release(), "4.0.2")

    @test.it("Rollbacks tests")
    def it_5():
        test.assert_equals(VersionManager().major().rollback().release(), "0.0.1")
        test.assert_equals(VersionManager().minor().rollback().release(), "0.0.1")
        test.assert_equals(VersionManager().patch().rollback().release(), "0.0.1")
        test.assert_equals(VersionManager().major().patch().rollback().release(), "1.0.0")
        test.assert_equals(VersionManager().major().patch().rollback().major().rollback().release(), "1.0.0")

    @test.it("Seperated calls")
    def it_6():
        m = VersionManager("1.2.3")
        m.major()
        m.minor()
        test.assert_equals(m.release(), "2.1.0")

    @test.it("Exception calls")
    def it_7():
        try:
            VersionManager("a.b.c")
            test.fail("Should throw when initial version cannot be parsed")
        except Exception as e:
            test.assert_equals(str(e),

"""
