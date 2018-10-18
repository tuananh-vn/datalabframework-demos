import datalabframework as dlf
dlf.project.profile('ingest-prod')
dlf.utils.pretty_print(dlf.params.metadata())
engine = dlf.engines.get('spark')
spark = engine.context()