from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_ranges_dont_overlap():
    first = time_range("2010-01-12 10:00:00","2010-01-12 10:00:00")
    second = time_range("2010-01-12 11:00:00", "2010-01-12 11:30:00")
    expected = []

    assert compute_overlap_time(first, second) == expected


import pytest
from times import time_range # 确保你导入了 time_range

##################////
# 把函数名改得更清晰
def test_time_range_backwards_raises_error():
    # 颠倒时间
    start_time = "2010-01-12 10:30:00"  # 晚的时间
    end_time = "2010-01-12 10:00:00"    # 早的时间

    # 现在这个测试是正确的：它期望一个 ValueError，
    # 并且 time_range 会提供一个
    # (确保 "match" 里的字符串和你函数中 raise 的错误消息完全一致)
    with pytest.raises(ValueError, match="end_time cannot be before start_time"):
        time_range(start_time, end_time)