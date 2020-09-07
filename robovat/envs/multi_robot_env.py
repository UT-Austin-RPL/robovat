"""Base environment for multi robot environments."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from robovat.envs import robot_env
from robovat.math import Pose
from robovat.robots import sawyer, franka_panda
from robovat.perception.camera import Kinect2
from robovat.simulation.camera import BulletCamera


class MultiRobotEnv(robot_env.RobotEnv):
    """The environment of multi robots."""

    def __init__(self,
                 simulator=None,
                 config=None,
                 debug=False):
        """Initialize

        """

        super(MultiRobotEnv, self).__init__(
            simulator=simulator,
            config=config,
            debug=debug)


        # Scene
        self.ground = None


    def reset(self):
        """Reset."""


    def step(self, aciton):
        """Take a step.

        Args:
           action: multi robots' actions

        """

        pass

    def get_observation(self):
        """Return observation for multi robots."""


    def get_reward(self):
        """Return Multi Robot rewards
        

        """
        reward = 0.0
        
