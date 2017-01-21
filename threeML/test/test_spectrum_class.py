import pytest
from threeML.plugins.spectrum.binned_spectrum import BinnedSpectrum, BinnedPoissonSpectrum, BinnedBackgroundSpectrum, BinnedPoissonBackgroundSpectrum
from threeML.plugins.spectrum.binned_spectrum_set import BinnedSpectrumSet


from threeML.io.file_utils import within_directory

import os

__this_dir__ = os.path.join(os.path.abspath(os.path.dirname(__file__)))


def test_spectrum_constructor():
    with within_directory(__this_dir__):


        # Create an instance of the GBM plugin for each detector
        # Data files
        obs_spectrum = "test.pha{1}"
        bak_spectrum = "test_bak.pha"
        #rsp_file =


        spectrum = BinnedSpectrum.from_fits_file(obs_spectrum, file_type='observed')

        assert isinstance(spectrum,BinnedPoissonSpectrum)

