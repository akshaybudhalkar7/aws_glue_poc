import awswrangler as wr

def main():
    # Define S3 paths
    source_s3_path = 's3://your-source-bucket/source-data.csv'
    target_s3_path = 's3://your-target-bucket/target-data.csv'

    # Read data from S3
    df = wr.s3.read_csv(source_s3_path)

    # Transform data
    df['transformed_column'] = df['existing_column'].apply(lambda x: x.upper())

    # Write data back to S3
    wr.s3.to_csv(df, target_s3_path)

if __name__ == "__main__":
    main()


