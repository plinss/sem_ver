# sem_ver

This package contains a parser for Semantic Version labels complete with type annotations. 

In addition to parsing version labels they may be compared via standard comparison operators 
and modified directly.
Note that comparison operators, including equality, do not consider build information.
To test for equality including build information, convert to, and compare strings.
SemVer objects may be directly compared to strings, or other objects that can be converted to strings,
a `ValueError` will be raised if the other object is not a valid SemVer.

See https://semver.org for details.

### sem_ver.SemVer

#### sem_ver.validate(version: str) -> bool

Test if string is a valid SemVer.

#### sem_ver.compare(version_a: str, version_b: str) -> int

Compare two SemVer strings.
Will raise `ValueError` if either string is not a valid SemVer.

#### sem_ver.force(version: str) -> Optional[SemVer]

Use relaxed parsing rules to attempt to create a SemVer.
Returns `None` if no version info found.

#### SemVer(version: str = None, major: int = 0, minor: int = 0, patch: int = 0, prerelease: Union[str, Sequence[Union[int, str]]] = '', build: Union[str, Sequence[str]] = '')

Constructor.
Will raise `ValueError` if the passed version string does not match the proper format.

#### SemVer.major: int

Major version.
Changing the major version will reset the minor, patch, prerelease, and build versions.

#### SemVer.minor: int

Minor version.
Changing the minor version will reset the patch, prerelease, and build versions.

#### SemVer.patch: int

Patch version.
Changing the patch version will reset the prerelease and build versions.

#### SemVer.prerelease: Optional[str]

Prerelease tags as a single string.
Will raise `ValueError` if the prerelease string does not match the proper format.

#### SemVer.prereleases: List[Union[int, str]]

Prerelease tags as a list of int or string.
Does not validate the strings.

#### SemVer.build: Optional[str]

Build labels as a single string.
Will raise `ValueError` if the build string does not match the proper format.

#### SemVer.builds: List[str]

Build labels as a list of strings.
Does not validate the strings.

#### SemVer.next_major() -> SemVer

Create a new SemVer for the next major release.
Minor, patch, prerelease, and build will be reset.

#### SemVer.next_minor() -> SemVer

Create a new SemVer for the next minor release.
Patch, prerelease, and build will be reset.

#### SemVer.next_patch() -> SemVer

Create a new SemVer for the next patch release.
Prerelease and build will be reset.

#### SemVer.__str__() -> str

Convert to string.

### Installation

Install with pip:

    pip install sem_ver