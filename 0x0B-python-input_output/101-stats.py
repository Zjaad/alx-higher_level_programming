#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After ten lines or the input of a keyboard interruption, 
prints the following statistics:
    - Total accumulated file size.
    - Count of accumulated status codes.
"""


def print_metrics(total_size, status_code_counts):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated total file size.
        status_code_counts (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(total_size))
    for code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_code_counts = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_code_counts)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in valid_status_codes:
                    if status_code not in status_code_counts:
                        status_code_counts[status_code] = 1
                    else:
                        status_code_counts[status_code] += 1
            except IndexError:
                pass

        print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code_counts)
        raise
