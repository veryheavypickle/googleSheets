import pandas as pd
import os
import pygsheets


def main():
    # Based on http://inquisitiveone.in/tutorial/tutorial-how-to-read-and-write-data-from-python-to-google-sheets/
    sheetID = "135iNOoGexE9_q1Se97SHmccVvLJq5rLLE2KJq25Aeww"
    if os.path.exists(AuthFile):
        openSheet(sheetID)
    else:
        print("You need to create a google thingy")
        print("https://pygsheets.readthedocs.io/en/stable/authorization.html")


def openSheet(sheetID):
    gc = pygsheets.authorize(service_file=AuthFile)
    sh = gc.open_by_key(sheetID)[0]
    # sh = gc.open("DeleteMePythonTest")[0]
    read = sh.get_as_df()
    print(read)


if __name__ == "__main__":
    AuthFile = "auth.json"
    main()
