import os
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "solution.sh"

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def test_multiple_files(tmp_path):
    d = tmp_path
    (d / "file1").write_text("A")
    (d / "file2").write_text("BB")
    (d / "file3").write_text("CCC")
    (d / "file4").write_text("DDDD")
    out = run(f"/bin/bash {SCRIPT} {d}")
    assert out.splitlines() == [
        f"4 {d}/file4",
        f"3 {d}/file3",
        f"2 {d}/file2",
    ]

def test_fewer_than_three(tmp_path):
    d = tmp_path
    (d / "file1").write_text("Hello")
    (d / "file2").write_text("World!")
    out = run(f"/bin/bash {SCRIPT} {d}")
    assert out.splitlines() == [
        f"6 {d}/file2",
        f"5 {d}/file1",
    ]

def test_empty_dir(tmp_path):
    out = run(f"/bin/bash {SCRIPT} {tmp_path}")
    assert out == ""

def test_current_dir(tmp_path):
    (tmp_path / "file1").write_text("X")
    (tmp_path / "file2").write_text("YY")
    cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        out = run(f"/bin/bash {SCRIPT}")
    finally:
        os.chdir(cwd)
    assert out.splitlines() == [
        f"2 {tmp_path}/file2",
        f"1 {tmp_path}/file1",
    ]

def test_nested(tmp_path):
    sub = tmp_path / "sub"
    sub.mkdir()
    (tmp_path / "file1").write_text("12345")
    (sub / "file2").write_text("6789")
    (sub / "file3").write_text("0")
    out = run(f"/bin/bash {SCRIPT} {tmp_path}")
    assert out.splitlines() == [
        f"5 {tmp_path}/file1",
        f"4 {sub}/file2",
        f"1 {sub}/file3",
    ]

def test_symlinks_and_special(tmp_path):
    f1 = tmp_path / "file1"
    f1.write_text("Data")
    symlink = tmp_path / "symlink"
    symlink.symlink_to(f1)
    # device node might need root, so please ignore failure
    subprocess.run(f"mknod {tmp_path}/device c 1 3", shell=True, check=False)
    out = run(f"/bin/bash {SCRIPT} {tmp_path}")
    assert out == f"4 {f1}"
