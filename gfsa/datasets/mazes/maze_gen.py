# coding=utf-8
# Copyright 2020 The Google Research Authors.
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

# Lint as: python3
"""Generating mazes using Labmaze."""

from typing import Optional

import labmaze
import numpy as np


def generate_small_labmaze(seed = None):
  """Generate a maze using labmaze.

  The dimensions of this maze have been set based on interactive exploration.
  Example maze generated by these sizes:

      ███████████████
      █   █ ███     █
    ███ ███ ███████ █
    ███ ███ ███ ███ █
    ███████████ █████
    ███ █   █   ███ █
    ███ █   █   ███ █
      █ █   █   █ █ █
      ███   █████ ███
      █         █ ███
      █         █ ███
      █         █ ███
      ███████████ ███
            █   █ █
      ███████   ███
      ███████
      ███████

  Args:
    seed: Random seed to use when generating the maze.

  Returns:
    Random maze, as a <bool[19, 19]> array.
  """
  grid_char_array = labmaze.random_maze.RandomMaze(
      width=19,
      height=19,
      max_rooms=6,
      room_min_size=3,
      room_max_size=8,
      random_seed=seed,
  ).entity_layer
  maze = (grid_char_array == " ")
  return maze