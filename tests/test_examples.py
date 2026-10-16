"""Przykłady uruchamiamy jako moduły, zgodnie z README."""

import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
MODULES = [".".join(path.relative_to(ROOT).with_suffix("").parts)
           for path in sorted((ROOT / "kodowanie").rglob("*.py"))]


@pytest.mark.parametrize("module", MODULES)
def test_example_runs_as_module(module):
    result = subprocess.run(
        [sys.executable, "-B", "-m", module],
        cwd=ROOT,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=15,
    )
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("script", ["kodowanie/generatory/example.py", "kodowanie/context_manager/function_example.py"])
def test_file_examples_work_outside_repository(script, tmp_path):
    result = subprocess.run(
        [sys.executable, "-B", str(ROOT / script)],
        cwd=tmp_path,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=15,
    )
    assert result.returncode == 0, result.stdout + result.stderr
