import extract
import silver
import gold


def main():
    print("Pipeline completo: extract -> silver -> gold")
    extract.main()
    silver.main()
    gold.main()
    print("Pipeline completo finalizado.")


if __name__ == "__main__":
    main()