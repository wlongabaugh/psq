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

from gcloud import pubsub
import psq

PROJECT_ID = 'your-project-id'

pubsub_client = pubsub.Client(project=PROJECT_ID)

q = psq.Queue(pubsub_client)

def main():
    q.enqueue("Hello, World")

if __name__ == '__main__':
    main()
