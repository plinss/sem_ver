#!/usr/bin/env python3
"""Run comprehensive test suite."""

import collections
from typing import Any, Tuple

from sem_ver import SemVer


Result = collections.namedtuple('Result', ('major', 'minor', 'patch', 'prerelease', 'build'))


def _pass(test: str, result: Any) -> None:
    print('  PASS: "{test}" == {result}'.format(test=test, result=str(result)))


def _fail(test: str, result: Any, expected: Any) -> None:
    print('* FAIL: "{test}" got: "{result}", expected: "{expected}"'.format(test=test, result=str(result),
                                                                            expected=str(expected)))


def _check(test: str, result: Any, expected: Any) -> Tuple[int, int]:
    if (result == expected):
        _pass(test, result)
        return (1, 0)
    _fail(test, result, expected)
    return (0, 1)


def _compare(test: str, ver: SemVer, result: Result) -> bool:
    if ((ver.major == result.major)
            and (ver.minor == result.minor)
            and (ver.patch == result.patch)
            and (ver.prerelease == result.prerelease)
            and (ver.build == result.build)):
        _pass(test, result)
        return True
    _fail(test, (ver.major, ver.minor, ver.patch, ver.prerelease, ver.build), result)
    return False


parse_tests = (
    ('0.0.0', Result(0, 0, 0, None, None)),
    ('1.0.0', Result(1, 0, 0, None, None)),
    ('1.10.99', Result(1, 10, 99, None, None)),
    ('1.2.3-1', Result(1, 2, 3, '1', None)),
    ('1.2.3-1.2', Result(1, 2, 3, '1.2', None)),
    ('1.2.3-alpha', Result(1, 2, 3, 'alpha', None)),
    ('1.2.3-alpha1pre', Result(1, 2, 3, 'alpha1pre', None)),
    ('1.2.3--0alpha', Result(1, 2, 3, '-0alpha', None)),
    ('1.2.3-alpha.1.pre', Result(1, 2, 3, 'alpha.1.pre', None)),
    ('1.2.3+build', Result(1, 2, 3, None, 'build')),
    ('1.2.3+build.000', Result(1, 2, 3, None, 'build.000')),
    ('1.2.3+build1test', Result(1, 2, 3, None, 'build1test')),
    ('1.2.3-alpha+build', Result(1, 2, 3, 'alpha', 'build')),

    ('1', None),
    ('1.0', None),
    ('1.00.00', None),
    ('1.01.01', None),
    ('1.0.0pre', None),
    ('1.0.0-', None),
    ('1.0.0-+', None),
)

compare_tests = (
    ('0.0.0', '1.0.0', True),
    ('1.0.0', '1.0.0', False),
    ('1.0.0', '1.0.0-alpha', False),
    ('0.10.10', '1.0.0', True),
    ('0.0.10', '0.1.0', True),
    ('1.0.0-1', '1.0.0-alpha', True),
    ('1.0.0-alpha', '1.0.0-beta', True),
    ('1.0.0-alpha', '1.0.0-alpha.alpha', True),
)


def _run_tests() -> Tuple[int, int]:
    pass_count, fail_count = 0, 0
    for test, result in parse_tests:
        try:
            ver = SemVer(test)
            if (result is None):
                _fail(test, ver, result)
                fail_count += 1
                continue

            if (_compare(test, ver, result)):
                pass_count += 1
            else:
                fail_count += 1

            if (str(ver) != test):
                _fail(test + ' -> str', str(ver), test)
                fail_count += 1

        except Exception as error:
            if (result is not None):
                _fail(test, error, result)
                fail_count += 1
            else:
                _pass(test, None)
                pass_count += 1

    for a, b, compare_result in compare_tests:
        try:
            if ((SemVer(a) < SemVer(b)) == compare_result):
                _pass('{a} < {b}'.format(a=a, b=b), compare_result)
                pass_count += 1
            else:
                _fail('{a} < {b}'.format(a=a, b=b), not compare_result, compare_result)
                fail_count += 1
        except Exception as error:
            _fail('Parse {a} or {b}'.format(a=a, b=b), error, '{a} {b}'.format(a=a, b=b))

    return (pass_count, fail_count)


if ('__main__' == __name__):      # called from the command line
    pass_count, fail_count = _run_tests()
    print('{passes} passes, {fails} failures'.format(passes=pass_count, fails=fail_count))
    if (fail_count):
        exit(1)
