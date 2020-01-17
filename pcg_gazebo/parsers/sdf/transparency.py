# Copyright (c) 2019 - The Procedural Generation for Gazebo authors
# For information on the respective copyright owner see the NOTICE file
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..types import XMLScalar


class Transparency(XMLScalar):
    _NAME = 'transparency'
    _TYPE = 'sdf'
    
    def __init__(self, default=0):
        XMLScalar.__init__(self, default=0)

    def _set_value(self, value):
        XMLScalar._set_value(self, value, min_value=0, max_value=1)
