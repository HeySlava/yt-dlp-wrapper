import contextlib
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Generator


DOCKER_IMAGE = 'yt-dlp-ffmpeg'


@contextlib.contextmanager
def download_folder(folder_name: str) -> Generator[Path, None, None]:
    path = Path(folder_name)
    path.mkdir(exist_ok=True)
    try:
        yield path
        files = path.glob('*')
        for file in files:
            destination = path.parent / file.name
            shutil.move(file, destination)
    finally:
        shutil.rmtree(path)


def main() -> int:
    if 'docker' not in sys.argv:
        cmd = ('yt-dlp', *sys.argv[1:])
        return subprocess.run(cmd).returncode

    with download_folder('./yt_dlp_dir') as yt_dlp_dir:
        yt_dlp_dir.mkdir(exist_ok=True)
        cmd = (
            'docker', 'run', '--rm',
            '-v', f'./{yt_dlp_dir.as_posix()}:/app',
            DOCKER_IMAGE, *sys.argv[2:]
        )

        p = subprocess.Popen(cmd)
        p.communicate()
    if p.returncode:
        print()
        print('=' * 79)
        print('Run `make build` in project directory')
    return p.returncode


if __name__ == '__main__':
    raise SystemExit(main())
