#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
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


import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):

    @task(1)
    def get_counts(self):
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ2aWQiOiIxMjM0NSIsImtpZCI6IkI0c1ZsdDNHMDFxOXdkblJaOXgwMWdjSUJXMDBGdVZRZXUzIn0.VGZX9p2LOUSVB-WCHXFz4S1oB-c_5_R3JkLrjUt3ZgMct-9fFEz82ro6yL7LJOho9cNAqKw-tA7bdmF-Cb6HH3cp-nS6XwR09Fvahv1aacRI4s21y6sgkpKS2WrMn5R0rjhHHXodHIdYTTrJ7nw9k7t1HVoc3K4jImy1XGXpOS9s8DTsCLHXhRhy8us0rYuNuOmncv7sNnigtV-8Tvw_Alt1V42-IsbtoOw8lxr2KSf-pw4zgufGubdYSpt4lRoOj2nBZYIJcFJptrj9uWoI6rTCk-VCU-sp2BGZ6MIMX2FuBglgQVuZMlgA8i1V457nZf9DkP9hLb9cIrfS85OyQg'
        self.client.get("/counts?token={0}".format(token))

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet