#!/usr/bin/env python

#
# Original implementation:
#
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
#
# Additional Material:
#
# Copyright 2017, Institute for Systems Biology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gcloud import pubsub
from psq.queue import Queue
from psq.task import Task

def main():
    PROJECT_ID = 'your-project-id'
    pubsub_client = pubsub.Client(project=PROJECT_ID)
    q = Queue(pubsub_client)
    for i in xrange(10):
        task = Task("Hello World A {}".format(i));
        q.enqueue(task)
    task = Task("Real Message");
    q.enqueue(task)
    for _ in xrange(10):
        task = Task("Hello World B {}".format(i));
        q.enqueue(task)

if __name__ == '__main__':
    main()
