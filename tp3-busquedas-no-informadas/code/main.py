from exploration import generate_random_map_custom
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from gymnasium import wrappers

env = generate_random_map_custom(100, 0.08)
env = wrappers.TimeLimit(env, 1000)
