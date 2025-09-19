import os
import subprocess
import tempfile
from pathlib import Path

def create_file(path: Path, size_bytes: int):
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.check_call(["dd", "if=/dev/zero", f"of={str(path)}", "bs=1", f"count={size_bytes}"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        with open(path, "wb") as f:
            f.write(b"\0" * size_bytes)

def run_solution_and_get_lines(test_dir: Path, target_dir: Path):
    sol_path = Path("/app/solution.sh")
    out = subprocess.check_output(["/bin/bash", str(sol_path), str(target_dir)]).decode().strip()
    if out == "":
        return []
    return out.splitlines()

def test_top_3_largest_files(tmp_path: Path):
    td = tmp_path / "sample"
    f1 = td / "a" / "file_small.txt"
    f2 = td / "b" / "file_medium.txt"
    f3 = td / "c" / "file_large.txt"
    f4 = td / "c" / "file_extra.txt"

    create_file(f1, 10)
    create_file(f2, 50)
    create_file(f3, 200)
    create_file(f4, 5)

    lines = run_solution_and_get_lines(Path(os.environ["TEST_DIR"]), td)

    assert len(lines) >= 3
    parts = [line.split(" ", 1) for line in lines[:3]]
    sizes = [int(p[0]) for p in parts]
    paths = [p[1] for p in parts]
    assert sizes == [200, 50, 10]
    for p in paths:
        assert os.path.isabs(p)
        assert os.path.exists(p)

def test_fewer_than_three_files(tmp_path):
    td = tmp_path / "smallset"
    f1 = td / "single.txt"
    create_file(f1, 123)
    out = subprocess.check_output(["/bin/bash", "/app/solution.sh", str(td)]).decode().strip()
    lines = out.splitlines() if out else []
    assert len(lines) == 1
    size_str, path_str = lines[0].split(" ", 1)
    assert int(size_str) == 123
    assert os.path.isabs(path_str)
    assert os.path.exists(path_str)
