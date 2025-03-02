# Copyright 2017 Iguazio
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
#
class ExceptionWithResponse(IOError):

    def __init__(self, status_code, body=None, content_type=None):
        self._status_code = status_code
        self._body = body
        self._content_type = content_type

    @property
    def body(self):
        return self._body

    @property
    def status_code(self):
        return self._status_code

    @property
    def content_type(self):
        return self._content_type
