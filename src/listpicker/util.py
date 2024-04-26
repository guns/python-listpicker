import regex

CSI_SGR_REGEX = regex.compile("\x1b\\[[\\d;]*m")
CSI_SGR_RESET = "\x1b[m"


def sgr_len(s: str) -> int:
    return len(CSI_SGR_REGEX.sub("", s))


def sgr_truncate(s: str, n: int) -> str:
    """
    Truncate string s to n non-SGR escape characters. O(n) worst-case performance.
    """
    if n >= len(s):
        return s

    dst = []
    cur_len = 0
    next_len = 0
    prev_stop = 0

    for m in CSI_SGR_REGEX.finditer(s):
        cur_start, cur_stop = m.span()
        next_len += cur_start - prev_stop

        if next_len >= n:
            dst.append(s[prev_stop : prev_stop + n - cur_len])
            dst.append(m.group(0) + CSI_SGR_RESET)
            return "".join(dst)

        dst.append(s[prev_stop:cur_start])
        dst.append(m.group(0))
        cur_len = next_len
        prev_stop = cur_stop

    dst.append(s[prev_stop : prev_stop + n - cur_len])

    if prev_stop:
        # We found at least one SGR escape, so SGR reset in case we are
        # truncating in the middle of an SGR pair.
        dst.append(CSI_SGR_RESET)

    return "".join(dst)


def plural_s(n: int, s: str = "s") -> str:
    "Pluralization helper"
    return "" if n == 1 else s


def smartcase_substring_match(substring: str, string: str) -> bool:
    # Disable case insensitivity when substring has an uppercase letter
    if regex.search(r"\p{Lu}", substring):
        return substring in string

    return substring in string.lower()


def bytes_to_int(*bs: int) -> int:
    "Parse a sequence of bytes as an integer"
    n = 0
    for b in bs:
        assert 0 <= b <= 255
        n <<= 8
        n |= b
    return n
