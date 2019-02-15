from gym.envs.registration import register

register(
	   id='MyLunarLanderContinuous-v2',
	entry_point='myenv.lunar_lander:LunarLanderContinuous',
)