import exifread
import argparse
import dateutil.parser as dparser
parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='f', type=str, nargs='+',
                    help='file names')
args = parser.parse_args()


# Open image file for reading (binary mode)
for filename in args.files:
    dparser.parse(filename)
    f = open(filename, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    print("{0} ".format(tags))
    for k, v in tags.items():
        print("{0} {1}".format(k, v))
    
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print("Key: {0} , value {1}".format(tag, tags[tag]))
