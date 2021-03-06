import unittest
import os
from tests.definitions import ROOT_DIR
from pydnameth.config.data.data import Data
from pydnameth.config.experiment.experiment import Experiment
from pydnameth.config.annotations.annotations import Annotations
from pydnameth.config.attributes.attributes import Observables
from pydnameth.config.attributes.attributes import Cells
from pydnameth.config.attributes.attributes import Attributes
from pydnameth.config.config import Config
from pydnameth.infrastucture.load.excluded import load_excluded
from pydnameth.infrastucture.path import get_data_base_path
from tests.tear_down import clear_cache


class TestLoadCpG(unittest.TestCase):

    def setUp(self):

        data = Data(
            path=ROOT_DIR,
            base='fixtures'
        )

        experiment = Experiment(
            data=None,
            task=None,
            method=None,
        )

        annotations = Annotations(
            name='annotations',
            exclude='none',
            cross_reactive='ex',
            snp='ex',
            chr='NS',
            gene_region='yes',
            geo='any',
            probe_class='any'
        )

        observables = Observables(
            name='observables',
            types={}
        )

        cells = Cells(
            name='cells',
            types='any'
        )

        attributes = Attributes(
            target='age',
            observables=observables,
            cells=cells
        )

        self.config = Config(
            data=data,
            experiment=experiment,
            annotations=annotations,
            attributes=attributes,
            is_run=True,
            is_root=True
        )
        self.config.initialize()

    def tearDown(self):
        clear_cache(self.config)

    def test_load_excluded_check_none_excluded(self):
        self.assertEqual([], load_excluded(self.config))

    def test_load_excluded_check_pkl_creation(self):
        self.config.annotations.exclude = 'excluded'
        fn = get_data_base_path(self.config) + '/' + self.config.annotations.exclude + '.pkl'

        self.config.excluded = load_excluded(self.config)

        self.assertEqual(True, os.path.isfile(fn))

    def test_load_excluded_check_len_excluded(self):
        self.config.annotations.exclude = 'excluded'

        self.config.excluded = load_excluded(self.config)

        self.assertEqual(3, len(self.config.excluded))
