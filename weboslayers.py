# Copyright (c) 2008-2024 LG Electronics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This implementation introduces next generation build environment for
# Open webOS. The change introduces a mechanism to add additional layers to the
# base ones: oe-core, meta-oe, and meta-webos, and to specify the commits to be
# used for each. mcf now expects the layers to be defined in this file
# (weboslayers.py in the same directory as mcf) as a list of Python data tuples:
#
# webos_layers = [
# ('layer-name', priority, 'URL', 'submission', 'working-dir'),
# ...
# ]
#
# where:
#
# layer-name  = Unique identifier; it represents the layer directory containing
#               conf/layer.conf.
#
# priority    = Integer layer priority as defined by OpenEmbedded. It also
#               specifies the order in which layers are searched for files.
#               Larger values have higher priority. A value of -1 indicates
#               that the entry is not a layer; for example, bitbake.
#
# URL         = The Git repository address for the layer from which to clone.
#               A value of '' skips the cloning.
#
# submission  = The information used by Git to checkout and identify the precise
#               content. Submission values could be "branch=<name>" and
#               "commit=<id>" or "tag=<tag>". Omitted branch information means
#               only that "master" will be used as the name of the local
#               branch. Omitted commit or tag means origin/HEAD will be checked
#               out (which might NOT be origin/master, although
#               it usually is).
#
# working-dir = Alternative directory for the layer.
#
# The name of the distribution is also defined in this file
# along with a list of the valid MACHINE-s
#

Distribution = "webos"

# Supported MACHINE-s
Machines = ['qemux86', 'qemux86-64', 'qemuarm', 'raspberrypi3', 'raspberrypi3-64', 'raspberrypi4', 'raspberrypi4-64']

# github.com/openembedded repositories are read-only mirrors of the authoritative
# repositories on git.openembedded.org
webos_layers = [
('bitbake',                   -1, 'https://github.com/openembedded/bitbake.git',            'branch=master,commit=f68b513c38f', ''),

('meta',                       5, 'https://github.com/openembedded/openembedded-core.git',  'branch=master,commit=546baa210ac', 'oe-core'),

('meta-oe',                   10, 'https://github.com/openembedded/meta-openembedded.git',  'branch=master,commit=4b64846ea75', 'meta-oe'),
('meta-multimedia',           11, 'https://github.com/openembedded/meta-openembedded.git',  '', 'meta-oe'),
('meta-networking',           12, 'https://github.com/openembedded/meta-openembedded.git',  '', 'meta-oe'),
('meta-python',               13, 'https://github.com/openembedded/meta-openembedded.git',  '', 'meta-oe'),
('meta-filesystems',          14, 'https://github.com/openembedded/meta-openembedded.git',  '', 'meta-oe'),

('meta-clang',                15, 'https://github.com/kraj/meta-clang.git',                 'branch=master,commit=e88c4d9795a', ''),
('meta-virtualization',       16, 'https://git.yoctoproject.org/git/meta-virtualization',   'branch=master,commit=9f23867e638', ''),

('meta-qt6',                  20, 'https://code.qt.io/yocto/meta-qt6.git',                  'branch=6.8.1,commit=f4ef1331f0c', ''),

('meta-webos',                40, 'https://github.com/shr-project/meta-webosose.git',       'branch=master,commit=master-2025-07-07', ''),

('meta-raspberrypi',          50, 'https://github.com/agherzan/meta-raspberrypi.git',       'branch=master,commit=49a2d124890', ''),
('meta-webos-raspberrypi',    51, 'https://github.com/shr-project/meta-webosose.git',       '', ''),
('meta-webos-virtualization', 53, 'https://github.com/shr-project/meta-webosose.git',       '', ''),

('meta-security',             76, 'https://git.yoctoproject.org/git/meta-security',         'branch=master,commit=ebe9234fb88', ''),
]
