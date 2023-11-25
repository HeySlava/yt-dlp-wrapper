import subprocess
import sys
from pathlib import Path


DOCKER_IMAGE = 'yt-dlp-ffmpeg'


def main() -> int:
    if 'docker' not in sys.argv:
        cmd = ('yt-dlp', *sys.argv[1:])
        return subprocess.run(cmd).returncode

    yt_dlp_dir = Path('./yt_dlp_dir')
    yt_dlp_dir.mkdir(exist_ok=True)
    cmd = (
        'docker', 'run', '--rm',
        '-v', fr'./{yt_dlp_dir.absolute().as_posix()}:/app',
        DOCKER_IMAGE, *sys.argv[2:]
    )
    print(cmd)

    p = subprocess.run(cmd)
    if p.returncode:
        print()
        print('=' * 79)
        print('Run `make build` in project directory')
    return p.returncode


if __name__ == '__main__':
    raise SystemExit(main())
