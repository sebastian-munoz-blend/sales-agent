def generate_csv(df):
    file_path = "output.csv"
    df.to_csv(file_path, index=False)
    return file_path