from clean import clean_data
from mapping import map_data
from validate import validate_data

def main():
    df = clean_data("data/raw/7020-NK-Th12.2025.xlsx")
    df = map_data(df, "data/master/master_product.xlsx")
    validate_data(df)
    df.to_excel("output/final_clean.xlsx", index=False)
    print("Done cleaning data!")

if __name__ == "__main__":
    main()