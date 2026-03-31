def validate_data(df):
    print("Missing values:")
    print(df.isnull().sum())

    print("Duplicate rows:", df.duplicated().sum())