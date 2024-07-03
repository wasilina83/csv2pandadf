import argparse
import pandas as pd

def read_csv_skip_first_row(csv_file):
    try:
        df = pd.read_csv(csv_file, skiprows=1)
        return df
    except FileNotFoundError:
        print(f"Datei '{csv_file}' nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei '{csv_file}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Einlesen einer CSV-Datei in ein Pandas DataFrame und Überspringen der ersten Zeile.")
    parser.add_argument("-f", "--file", type=str, required=True, help="Pfad zur CSV-Datei, die eingelesen werden soll")
    
    args = parser.parse_args()

    # Aufruf der Funktion zum Einlesen der CSV-Datei
    dataframe = read_csv_skip_first_row(args.file)
    
    if dataframe is not None:
        print("Daten erfolgreich eingelesen:")
        print(dataframe.head())  # Zeigt die ersten paar Zeilen des DataFrames an

if __name__ == "__main__":
    main()
