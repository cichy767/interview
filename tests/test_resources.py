import io
import sys

import pytest

from kodowanie.context_manager.function_example import own_open
from kodowanie.generatory import example
from kodowanie.generatory.help import mem_profile


@pytest.fixture
def records_file(monkeypatch):
    file = io.StringIO("ignored\ninfo:żółć\nwarning:a:b\n")
    monkeypatch.setattr(example, "open", lambda *args, **kwargs: file, raising=False)
    return file


def test_records_close_file_after_exhaustion(records_file):
    assert list(example.get_records("sample.txt")) == [("info", "żółć"), ("warning", "a:b")]
    assert records_file.closed


def test_records_close_file_when_generator_is_closed_early(records_file):
    generator = example.get_records("sample.txt")
    assert next(generator) == ("info", "żółć")
    assert not records_file.closed
    generator.close()
    assert records_file.closed


def test_records_close_file_on_exception(records_file):
    generator = example.get_records("sample.txt")
    next(generator)
    with pytest.raises(RuntimeError, match="interrupted"):
        generator.throw(RuntimeError("interrupted"))
    assert records_file.closed


def test_records_read_real_utf8_file(tmp_path):
    source = tmp_path / "records.txt"
    source.write_text("info:zażółć\n", encoding="utf-8")
    assert list(example.get_records(source)) == [("info", "zażółć")]


def test_records_empty_file(tmp_path):
    source = tmp_path / "empty.txt"
    source.write_text("", encoding="utf-8")
    assert list(example.get_records(source)) == []


def test_own_open_closes_file_after_exception(tmp_path):
    path = tmp_path / "example.txt"
    with pytest.raises(RuntimeError):
        with own_open(path, "w", encoding="utf-8") as file:
            file.write("żółć")
            raise RuntimeError("interrupted")
    assert file.closed
    assert path.read_text(encoding="utf-8") == "żółć"


def test_own_open_supports_binary_files(tmp_path):
    path = tmp_path / "example.bin"
    with own_open(path, "wb") as file:
        file.write(b"\x00\xff")
    assert file.closed
    assert path.read_bytes() == b"\x00\xff"


def test_memory_profile_returns_positive_rss():
    assert mem_profile.memory_usage_psutil() > 0


def test_resource_memory_profile_platform_support():
    if sys.platform == "win32":
        with pytest.raises(NotImplementedError, match="Windows"):
            mem_profile.memory_usage_resource()
    else:
        assert mem_profile.memory_usage_resource() > 0
