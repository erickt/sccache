#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re
from setuptools import setup
from pip.req import parse_requirements

with open('sccache/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='sccache',
    version=version,
    license='MPL',
    packages=[
        'sccache',
    ],
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'sccache = sccache.cli:main',
        ],
    }
)
