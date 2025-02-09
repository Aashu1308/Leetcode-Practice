import re
class Solution:
    def defangIPaddr(self, address: str) -> str:
        pattern=r"\."
        sub="[.]"
        return re.sub(pattern,sub,address)