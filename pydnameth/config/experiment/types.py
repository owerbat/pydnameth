from enum import Enum
from pydnameth.setup.advanced.clock.types import ClockExogType


class Task(Enum):
    table = 'table'
    clock = 'clock'
    observables = 'observables'
    methylation = 'methylation'
    dependence_2d = 'dependence_2d'

    def __str__(self):
        return str(self.value)


class Method(Enum):
    linreg = 'linreg'
    variance_linreg = 'variance_linreg'
    cluster = 'cluster'
    histogram = 'histogram'
    scatter = 'scatter'
    polygon = 'polygon'
    special = 'special'
    z_test = 'z_test'

    def __str__(self):
        return str(self.value)


class DataType(Enum):
    cpg = 'cpg'
    gene = 'gene'
    bop = 'bop'
    suppl = 'suppl'
    cache = 'cache'
    attributes = 'attributes'

    def __str__(self):
        return str(self.value)


def get_metrics_keys(setup):
    metrics = []

    if setup.task == Task.table:

        if setup.method == Method.linreg:
            metrics = [
                'item',
                'aux',
                'R2',
                'intercept',
                'slope',
                'intercept_std',
                'slope_std',
                'intercept_p_value',
                'slope_p_value'
            ]
        elif setup.method == Method.variance_linreg:
            metrics = [
                'item',
                'aux',
                'R2',
                'intercept',
                'slope',
                'intercept_std',
                'slope_std',
                'intercept_p_value',
                'slope_p_value',
                'R2_var',
                'intercept_var',
                'slope_var',
                'intercept_std_var',
                'slope_std_var',
                'intercept_p_value_var',
                'slope_p_value_var'
            ]
        elif setup.method == Method.cluster:
            metrics = [
                'item',
                'aux',
                'number_of_clusters',
                'number_of_noise_points',
            ]
        elif setup.method == Method.polygon:
            metrics = [
                'item',
                'aux',
                'area_intersection_rel',
                'slope_intersection_rel',
                'max_abs_slope'
            ]
        elif setup.method == Method.special:
            metrics = [
                'item'
            ]
        elif setup.method == Method.z_test:
            metrics = [
                'item',
                'aux',
                'z_value',
                'p_value'
            ]

    elif setup.task == Task.clock:

        if setup.method == Method.linreg:
            metrics = [
                'item',
                'aux',
                'R2',
                'r',
                'evs',
                'mae',
                'summary'
            ]

    return metrics


def get_main_metric(setup):
    metric = ()

    if setup.task == Task.table:

        if setup.method == Method.linreg:
            metric = ('R2', 'descending')
        elif setup.method == Method.variance_linreg:
            metric = ('R2_var', 'descending')
        elif setup.method == Method.cluster:
            metric = ('number_of_clusters', 'descending')
        elif setup.method == Method.polygon:
            metric = ('area_intersection_rel', 'ascending')
        elif setup.method == Method.z_test:
            metric = ('p_value', 'ascending')

    return metric


def get_default_params(setup):
    params = {}

    if setup.task == Task.table:

        if setup.method == Method.cluster:
            params = {
                'eps': 0.2,
                'min_samples': 5
            }
        elif setup.method == Method.polygon:
            params = {}

    elif setup.task == Task.clock:

        if setup.method == Method.linreg:
            params = {
                'type': ClockExogType.all.value,
                'part': 0.25,
                'exogs': 100,
                'combs': 100,
                'runs': 100,
            }

    elif setup.task == Task.observables:

        if setup.method == Method.scatter:
            params = {
                'item': 'cg01620164',
                'x_range': [0, 100]
            }

    elif setup.task == Task.dependence_2d:

        if setup.method == Method.scatter:
            params = {
                'x': 'count',
                'y': 'count',
            }

    return params
