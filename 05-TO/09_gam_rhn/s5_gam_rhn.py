import sys
sys.path.append('../../')

from tframe.utils.script_helper import Helper
from tframe.trainers.trainer import TrainerHub as Config


Helper.register_flags(Config)
s = Helper()
# -----------------------------------------------------------------------------
# Configure data set here
# -----------------------------------------------------------------------------
s.register('max_iterations', 50000)

s.register('bits', 3)
s.register('sequence_length', 100)
# -----------------------------------------------------------------------------
# Specify summary file name and GPU ID here
# -----------------------------------------------------------------------------
summ_name = s.default_summ_name
gpu_id = 0

s.register('gather_summ_name', summ_name + '.sum')
s.register('gpu_id', gpu_id)
# -----------------------------------------------------------------------------
# Set up your models and run
# -----------------------------------------------------------------------------
s.register('gam_config', '6x10')
s.register('head_size', 20)
# s.register('sog_version', 0)

s.register('hyper_kernel', 'gru')
s.register('state_size', 60)
s.register('num_layers', 1, 2, 3, 4, 5, 6)

s.register('lr', 0.001)

s.run(50)
