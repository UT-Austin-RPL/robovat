Quick Introduction by Example
=============================

Overview
---------

Environment creation
--------------------
Here we will just go through a simple overview of the environment
creation.

A robovat environment is derived from a class `arm_env.ArmEnv`.


Then add the import of environments in the
file `robotvat/envs/__init__.py_`:

::
   
   from .FOLDER.FILE_NAME import ENV_NAME


Grasping Explanation
----------------

Here we explain more on the details of grasping objects. Simulation is
not perfect. So you need to take care with some parameters to make
simulation work more like in the real-world.



For visualizing an example of grasping an object, you can run:

.. code-block:: bash
                
                python tools/demo_grasp.py --env FrankaPandaGraspEnv --debug 1 --env_config configs/envs/franka_panda_envs/franka_panda_grasp_env.yaml


Pushing Explanation
-------------------



.. code-block:: bash
                
                python tools/demo_push.py --env FrankaPandaPushEnv --policy HeuristicPushPolicy --debug 1 --env_config configs/envs/franka_panda_envs/franka_panda_push_env.yaml
                
