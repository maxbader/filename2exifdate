import argparse
import os


def get_file_date_str(filename, format):
    format_list = list(format)
    filename_list = list(filename)
    year = str()
    month = str()
    day = str()
    hour = str()
    min = str()
    sec = str()
    milli = str()
    date_str = str()
    for i in range(0, len(format_list)):
        c = filename_list[i]
        if c.isdigit():
            if format_list[i] == 'Y': year = year + c
            elif format_list[i] == 'M': month = month + c
            elif format_list[i] == 'D': day = day + c
            elif format_list[i] == 'h': hour = hour + c
            elif format_list[i] == 'm': min = min + c
            elif format_list[i] == 's': sec = sec + c
            elif format_list[i] == 'c': milli = milli + c
            else : return str()
            
    if len(year)  != 4: year = '1970'
    if len(month) != 2: month = '01'
    if len(day) != 2: day = '01'
    if len(hour) != 2: hour = '00'
    if len(min) != 2: min = '00'
    if len(sec) != 2: sec = '00'
    if len(milli) == 0: milli = '00'

    date_str = year + '-' + month + '-' + day + ' ' + hour + ':' + min + ':' + sec + '-' + milli
    return date_str



def set_exif_date(filename, date_str, date_tags, exifcmd, echo, echo_only):

    command = exifcmd + " -overwrite_original "
    for tag in date_tags:
        command = command + "'-" + tag + "=" + date_str + "' "
    command = command + " " + filename
    if echo or echo_only:
        print(command)
    if not echo_only:
        os.system(command)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', metavar='i', type=str, nargs='+', required=True, help='input file')
    parser.add_argument("--prefix", metavar='p', type=str, default='signal-', help="file prefix")
    parser.add_argument("--format", metavar='f', type=str, default='YYYY-MM-DD-hh-mm-ss-ccc', help="date format YYYY-MM-DD-hh-mm-ss-ccc")
    parser.add_argument("--exifcmd", type=str, default='exiftool', help="exiftool command")
    parser.add_argument('--date_tags', type=str, nargs='+', default=['alldates'],  help='exif tags to set such as alldates, FileModifyDate, CreateDate, ...')
    parser.add_argument('--echo', action='store_true', help="prints the exiftool command")
    parser.add_argument('--echo_only', action='store_true', help="used to prevent the command execution")
    args = parser.parse_args()

    for filename in args.input:
        basename = os.path.basename(filename)
        date_str = get_file_date_str(basename.replace(args.prefix, ""), args.format)
        if not date_str:
            print("Error: check the date format: {}{} and the file name: {}".format(args.prefix, args.format, filename))
            exit()
        set_exif_date(filename, date_str, args.date_tags, args.exifcmd, args.echo, args.echo_only)


if __name__ == "__main__":
    main()
