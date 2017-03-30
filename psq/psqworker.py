#!/usr/bin/env python

# Copyright 2015 Google Inc.
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

from __future__ import absolute_import

from importlib import import_module
import os
import sys

def import_queue(location):
    module, attr = location.rsplit('.', 1)
    module = import_module(module)
    queue = getattr(module, attr)
    if hasattr(queue, '__call__'):
        queue = queue()
    return queue


def main(path, single_threaded, workers, pid, queue):
    """
    Standalone PSQ worker
    """
    setup_logging()
    # temporary hack
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path = [x for x in sys.path if not x == here]

    if not path:
        path = os.getcwd()

    sys.path.insert(0, path)

    queue = import_queue(queue)

    import psq

    worker = psq.Worker(queue=queue)
    
    worker.listen()


if __name__ == '__main__':
    main()
