from sqlite3 import connect, Error
from datetime import datetime
from time import sleep

def create_connection(db_file):
    conn = None
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    return conn


def getOldestUnclassifiedImage(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM web_image WHERE classification = \'waiting for classification\' ORDER BY dateAdded LIMIT 1")
    result = cur.fetchone()
    cur.close()
    return result


def getClassification(imgPath):
    #TODO: call the neural network
    result = "classified"
    return result

def classifyImage(row, asInProgress = False):
    id = row[0]
    # title = row[1]
    # dateAdded = row[2]
    imgPath = "uploads/" + row[3]
    classification = row[4]
    dateClassified = row[5]
    # userId = row[6]

    classification = "in progress" if asInProgress else getClassification(imgPath)
    return (id, classification)


def updateImage(result, conn):
    id, classification = result
    now = datetime.now()
    conn.execute(f"UPDATE web_image SET classification = '{classification}', dateClassified = '{now}' WHERE id = {id};")
    conn.commit()
    print(f"{id} : {classification} : {now}")


def main():
    database = "db.sqlite3"
    conn = create_connection(database)
    with conn:
        while (True):
            img = getOldestUnclassifiedImage(conn)

            if (img is not None):
                imgInProgress = classifyImage(img, True)
                updateImage(imgInProgress, conn)

                imgClassified = classifyImage(img)
                updateImage(imgClassified, conn)
            else:
                print("no image to classify")
            
            sleep(0.5)
        

if __name__ == '__main__':
    main()