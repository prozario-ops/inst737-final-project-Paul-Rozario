from src.etl.extract import extract
from src.etl.transform import transform


def main():

    data=extract()
    if data:
        print("Data extraction successful.")
    else:
        print("Data extraction failed.")
    #transformed=transform(data)
    

if __name__ == "__main__":
    main()