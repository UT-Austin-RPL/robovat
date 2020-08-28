#!/usr/bin/env python

"""
Run an environment with the chosen policy.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import ast
import os
import random
import socket
import uuid
from builtins import input

import numpy as np
import h5py

import _init_paths  # NOQA
from robovat import envs
from robovat import policies
from robovat.io import hdf5_utils
from robovat.io.episode_generation import generate_episodes
from robovat.simulation.simulator import Simulator
from robovat.utils import time_utils
from robovat.utils.logging import logger
from robovat.utils.yaml_config import YamlConfig

import matplotlib.pyplot as plt

def parse_args():
    """Parse arguments.

    Returns:
        args: The parsed arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--env',
        dest='env',
        type=str,
        help='The environment.',
        required=True)

    parser.add_argument(
        '--policy',
        dest='policy',
        type=str,
        help='The policy.',
        default=None)

    parser.add_argument(
        '--env_config',
        dest='env_config',
        type=str,
        help='The configuration file for the environment.',
        default=None)

    parser.add_argument(
        '--policy_config',
        dest='policy_config',
        type=str,
        help='The configuration file for the policy.',
        default=None)

    parser.add_argument(
        '--config_bindings',
        dest='config_bindings',
        type=str,
        help='The configuration bindings.',
        default=None)

    parser.add_argument(
        '--use_simulator',
        dest='use_simulator',
        type=int,
        help='Run experiments in the simulation is it is True.',
        default=1)

    parser.add_argument(
        '--assets',
        dest='assets_dir',
        type=str,
        help='The assets directory.',
        default='./assets')

    parser.add_argument(
        '--output',
        dest='output_dir',
        type=str,
        help='The output directory to save the episode history.',
        default=None)

    parser.add_argument(
        '--num_steps',
        dest='num_steps',
        type=int,
        help='Maximum number of time steps for each episode.',
        default=None)

    parser.add_argument(
        '--num_episodes',
        dest='num_episodes',
        type=int,
        help='Maximum number of episodes.',
        default=None)

    parser.add_argument(
        '--num_episodes_per_file',
        dest='num_episodes_per_file',
        type=int,
        help='The maximum number of episodes saved in each file.',
        default=1000)

    parser.add_argument(
        '--debug',
        dest='debug',
        type=int,
        help='True for debugging, False otherwise.',
        default=0)

    parser.add_argument(
        '--worker_id',
        dest='worker_id',
        type=int,
        help='The worker ID for running multiple simulations in parallel.',
        default=0)

    parser.add_argument(
        '--seed',
        dest='seed',
        type=int,
        help='None for random; any fixed integers for deterministic.',
        default=None)

    parser.add_argument(
        '--pause',
        dest='pause',
        type=bool,
        help='Whether to pause between episodes.',
        default=False)

    parser.add_argument(
        '--timeout',
        dest='timeout',
        type=float,
        help='Seconds of timeout for an episode.',
        default=120)

    args = parser.parse_args()

    return args


def parse_config_files_and_bindings(args):
    if args.env_config is None:
        env_config = None
    else:
        env_config = YamlConfig(args.env_config).as_easydict()

    if args.policy_config is None:
        policy_config = None
    else:
        policy_config = YamlConfig(args.policy_config).as_easydict()

    if args.config_bindings is not None:
        parsed_bindings = ast.literal_eval(args.config_bindings)
        logger.info('Config Bindings: %r', parsed_bindings)
        env_config.update(parsed_bindings)
        policy_config.update(parsed_bindings)

    return env_config, policy_config


def main():
    args = parse_args()

    # Configuration.
    env_config, policy_config = parse_config_files_and_bindings(args)

    # Set the random seed.
    if args.seed is not None:
        random.seed(args.seed)
        np.random.seed(args.seed)

    # Simulator.
    if args.use_simulator:
        simulator = Simulator(worker_id=args.worker_id,
                              use_visualizer=bool(args.debug),
                              assets_dir=args.assets_dir)
    else:
        simulator = None

    # Environment.
    env_class = getattr(envs, args.env)
    env = env_class(simulator=simulator,
                    config=env_config,
                    debug=args.debug)

    obs = env.reset()

    # Example of plotting visual observation
    plt.imshow(np.squeeze(obs[env.config.OBSERVATION.TYPE]))
    plt.show()

    # Move the end-effector to the center of table
    end_effector_pose = env.robot.end_effector.pose.copy()
    end_effector_pose.x = 0.5
    end_effector_pose.y = 0.0
    env.execute_moving_action(end_effector_pose)

    # Grasp the object
    object_pose = env.graspable.pose.copy()
    end_effector_pose = env.robot.end_effector.pose.copy()
    end_effector_pose.x = object_pose.x
    end_effector_pose.y = object_pose.y
    # Height is hard-coded here
    end_effector_pose.z = object_pose.z + 0.1
    env.execute_gentle_grasping_action(end_effector_pose)
    

if __name__ == '__main__':
    main()
