# file name to exif date
This python script is able to parse file names of date timestamps.
If a timestamp is used it can execute the _exiftool_ command to write exif date entries in your media files.
## Usage
```
usage: filenamedate2exifdate.py [-h] --input i [i ...] [--prefix p] [--format f] [--exifcmd EXIFCMD] [--date_tags DATE_TAGS [DATE_TAGS ...]] [--echo] [--echo_only]

options:
  -h, --help            show this help message and exit
  --input i [i ...]     input file --> required
  --prefix p            file prefix
  --format f            date format YYYY-MM-DD-hh-mm-ss-ccc
  --exifcmd EXIFCMD     exiftool command
  --date_tags DATE_TAGS [DATE_TAGS ...]
                        exif tags to set such as alldates, FileModifyDate, CreateDate, ...
  --echo                prints the exiftool command
  --echo_only           used to prevent the command execution
```
### Examples
#### Single files
Signal images
```
python ./filenamedate2exifdate.py --echo_only --prefix signal- --format YYYY-MM-DD-hh-mm-ss-ccc --date_tags alldates FileModifyDate --input signal-2021-02-20-08-59-20-104.jpg 
```
WhatsApp images
```
python ./filenamedate2exifdate.py --echo_only --prefix IMG- --format YYYYMMDD-WAcccc --date_tags alldates FileModifyDate --input IMG-20190721-WA0002.jpg 
```
WhatsApp video
```
python ./filenamedate2exifdate.py --echo_only --prefix VID- --format YYYYMMDD-WAcccc --date_tags alldates FileModifyDate --input VID-20190609-WA0019.mp4 
```
#### Patch processing
Signal images
```
find . -name 's*.jpg' -exec python ./filenamedate2exifdate.py --echo_only --prefix signal- --format YYYY-MM-DD-hh-mm-ss-ccc --date_tags alldates FileModifyDate --input {} \;
```
WhatsApp images
```
find . -name 'I*.jpg' -exec python ./filenamedate2exifdate.py --echo_only --prefix IMG- --format YYYYMMDD-WAcccc --date_tags alldates FileModifyDate --input {} \;
```
WhatsApp video
```
find . -name 'V*.mp4' -exec python ./filenamedate2exifdate.py --echo_only --prefix VID- --format YYYYMMDD-WAcccc --date_tags alldates FileModifyDate --input {} \;
```

## useful commands

```
rename 'y/A-Z/a-z/' *     # to lower case
rename 's/.jpeg/.jpg/' *  # jpeg to jpg
exiftool -overwrite_original -Artist="Max M" -Copyright="Max M" -Author="Max M"  *.{jpg,mp4}
exiftool signal-*.jpg '-FileName<CreateDate'       -ext jpg -d "%Y-%m-%d--%H-%M-%S-%%-.c.%%e"
exiftool IMG-*.jpg '-FileName<CreateDate'       -ext jpg -d "%Y-%m-%d--%H-%M-%S-%%-.c.%%e"
exiftool VID-*.mp4 '-FileName<CreateDate'       -ext mp4 -d "%Y-%m-%d--%H-%M-%S-%%-.c.%%e"
```



