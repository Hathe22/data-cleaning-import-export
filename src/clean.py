import pandas as pd

def clean_data(file_path):
    df = pd.read_excel(file_path)

    # Xóa dòng rỗng
    df = df.dropna(how='all')

    # Chuẩn hóa tên cột
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Chuẩn hóa text
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    return df