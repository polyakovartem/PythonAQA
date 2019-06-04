import sys
import csv
import os
import hashlib


def chunk_reader(file_object, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = file_object.read(chunk_size)
        if not chunk:
            return
        yield chunk


def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    duplicates_container = []
    skipped = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            print("Analyzing {}".format(dirpath))
            for each_file in filenames:
                full_path = os.path.join(dirpath, each_file)
                hashed_object = hash()

                try:
                    for chunk in chunk_reader(open(full_path, 'rb')):
                        hashed_object.update(chunk)
                except (OSError, RuntimeError):
                    print("Error: File does not appear to exist.")

                file_id = (hashed_object.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)

                try:
                    if duplicate:
                        print("Duplicate found: %s and %s"
                              % (full_path, duplicate))
                        text_to_append = "This file: {} has a " \
                                         "duplicated friend: {}"\
                            .format(full_path, duplicate)
                        duplicates_container.append(text_to_append)
                    else:
                        hashes[file_id] = full_path
                except (PermissionError, OSError):
                    skipped.append(full_path)
    return duplicates_container, skipped


def write_to_csv(duplicated_files, skipped_files):
    # Write the list of duplicate files to csv file
    try:
        with open("duplicates.csv", "w", encoding='utf-8') as log:
            csv_writer = csv.writer(log, quoting=csv.QUOTE_MINIMAL,
                                    delimiter=",",
                                    lineterminator="\n")
            # write duplicated files in .csv file
            header = ["File Names:"]
            csv_writer.writerow(header)
            for value in duplicated_files:
                csv_writer.writerow([value])

            if skipped_files:
                # write skipped files in .csv file
                header = ["Skipped Files:"]
                csv_writer.writerow(header)
                for value in skipped_files:
                    csv_writer.writerow([value])
        print("Done")
    except (OSError, RuntimeError):
        print("Error: File does not appear to exist.")


if sys.argv[1:]:
    duplicates, skipped = check_for_duplicates(sys.argv[1:])
    write_to_csv(duplicates, skipped)
else:
    print("Please pass the paths to check as parameters to the script")
