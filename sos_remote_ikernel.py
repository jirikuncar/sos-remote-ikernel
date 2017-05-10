import os

from sos.Python3.kernel import sos_Python3


class sos_PythonSlurm(sos_Python3):
    """Custom Python remote kernel using SLURM."""

    def __init__(self, *args, **kwargs):
        """Create kernel wrapper with configurable name and color."""
        super(sos_PythonSlurm, self).__init__(*args, **kwargs)
        self.kernel_name = os.getenv('SOS_PYTHON_SLURM_NAME', 'python_slurm')
        self.background_color = os.getenv('SOS_PYTHON_SLURM_COLOR', '#00FA05')
