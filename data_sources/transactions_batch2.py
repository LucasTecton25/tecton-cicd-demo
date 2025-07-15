from tecton import BatchSource, FileConfig


transactions_batch2 = BatchSource(
    name="transactions_batch2",
    batch_config=FileConfig(
        uri="s3://tecton.ai.public/tutorials/transactions.pq",
        file_format="parquet",
        timestamp_field="timestamp",
    ),
)