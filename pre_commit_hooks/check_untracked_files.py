import argparse
from collections.abc import Sequence
from os import unsetenv
import subprocess


def check_untracked_files(filenames, no_fail=False):
    process = subprocess.run(
        ('git', 'ls-files', '--others', '--exclude-standard'),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        encoding='utf-8',
        check=True,
    )
    stdout = process.stdout.strip('\n')
    untracked_files = stdout.split('\n') if stdout else []
    if len(untracked_files) > 0:
        print(
            f"{"WARN: " if no_fail else ""}Untracked files, please add, stash, or ignore.\n"
        )
        for filename in untracked_files:
            print(f"  - {filename}")
        return 0 if no_fail else 1
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('filenames', nargs='*')
    parser.add_argument(
        '--no-fail',
        action='store_true',
        help="Warn, don't fail.",
    )
    args = parser.parse_args(argv)

    return check_untracked_files(
        filenames=args.filenames,
        no_fail=args.no_fail,
    )


if __name__ == '__main__':
    raise SystemExit(main())
