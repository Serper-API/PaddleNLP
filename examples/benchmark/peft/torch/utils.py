# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

from transformers import Trainer


class CustomTrainer(Trainer):
    total_observed_tokens = 0.0

    def training_step(self, model, inputs):
        input_ids = inputs["input_ids"]
        self.total_observed_tokens += float(input_ids.shape[0] * input_ids.shape[1])
        return super().training_step(model, inputs)
