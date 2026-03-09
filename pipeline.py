from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline():

    print("Extracting data from API...")
    data = extract_data()

    print("Transforming data...")
    df = transform_data(data)

    print("Loading data into DuckDB...")
    load_data(df)

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()