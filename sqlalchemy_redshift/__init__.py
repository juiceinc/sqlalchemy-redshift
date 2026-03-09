from importlib.metadata import PackageNotFoundError as DistributionNotFound, version as _version
from packaging.version import Version as parse_version

def get_distribution(name):
    class _Dist:
        def __init__(self, n):
            self.version = _version(n)
    return _Dist(name)

for package in ['psycopg2', 'psycopg2-binary', 'psycopg2cffi']:
    try:
        if get_distribution(package).parsed_version < parse_version('2.5'):
            raise ImportError('Minimum required version for psycopg2 is 2.5')
        break
    except DistributionNotFound:
        pass

__version__ = get_distribution('sqlalchemy-redshift').version

from sqlalchemy.dialects import registry  # noqa

registry.register(
    "redshift", "sqlalchemy_redshift.dialect",
    "RedshiftDialect_psycopg2"
)
registry.register(
    "redshift.psycopg2", "sqlalchemy_redshift.dialect",
    "RedshiftDialect_psycopg2"
)
registry.register(
    'redshift+psycopg2cffi', 'sqlalchemy_redshift.dialect',
    'RedshiftDialect_psycopg2cffi',
)

registry.register(
    "redshift+redshift_connector", "sqlalchemy_redshift.dialect",
    "RedshiftDialect_redshift_connector"
)
