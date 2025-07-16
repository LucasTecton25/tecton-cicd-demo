from tecton import BatchSource, FileConfig


transactions_batch3 = BatchSource(
    name="transactions_batch3",
    batch_config=FileConfig(
        uri="s3://tecton.ai.public/tutorials/transactions.pq",
        file_format="parquet",
        timestamp_field="timestamp",
    ),
)

# git add entities/entity.py
# git add .github/workflows/tecton_build.yml
# git commit -m "Adding the first Tecton object entity.py"
# git push -u origin create-user-entity