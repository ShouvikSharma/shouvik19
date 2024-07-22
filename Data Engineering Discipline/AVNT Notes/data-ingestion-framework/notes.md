### Data-Ingestion Framework

1. Ingestion of the database and file framework is done via. a yaml file.
2. This model creates ingestion tools to democratize the ingestion framework to the DNA organization.
3. It entirely runs on [airflow2](https://airflow.apache.org/blog/airflow-two-point-oh-is-here/).
4. Ingestion proceeds with reading of the config file.
-  Source schema is checked with the bronze table, to gauge whether there any schema breaking changes.
-  for each entry in the yaml file, the plan of action would be to either insert into the bronze layer, merge into the silver layer and create vdses and pdses in dremio.
