
from datetime import datetime

# [TODO]: step 1
# Update the is_log_line function below to skip lines that are not valid log lines.
# Valid log lines have a timestamp, error type, and message. For example, lines 1, 3,
# 7 and 37 are all examples of lines (from sample.log) that would be filtered out.
# There's no perfect way to do this: just decide what you think is reasonable to get
# the test to pass. The only thing you are not allowed to do is filter out log lines
# based on the exact row numbers you want to remove.

VALID_LOG_LEVELS = (
    "INFO",
    "TRACE",
    "WARNING"
)
VALID_DATE_FORMAT = "%d/%m/%y"
VALID_TIME_FORMAT = "%H:%M:%S"


def get_message_from_line(line: str) -> str:
    """
    Function to return message from given line, or an empty string if there is no message (or if
    the message is just white space);
    """
    if not " :" in line:
        return ""
    
    message = " :".join(line.split(" :")[1:])
    if not message.strip():
        return ""
    
    return ":" + message


def get_timestamp_from_line(line: str) -> str:
    """
    
    """


def validate_timestamp(date_string: str, time_string: str) -> bool:
    """
    Function to check whether a given date string and time string match the timestamp format
    required.
    """
    try:
        datetime.strptime(date_string, VALID_DATE_FORMAT)
        datetime.strptime(time_string, VALID_TIME_FORMAT)
        return True
    except ValueError:
        return False


def is_log_line(line):
    """
    Takes a log line and returns True if it is a valid log line and returns nothing if it is not;
    """

    if not get_message_from_line(line):
        return None
    
    fields = line.split(" :")[0].split(" ")


    
    # Check there is a valid timestamp - we don't care where, but time must follow date
    count = 0
    bln_criterion_met = False
    while not bln_criterion_met:
        date = fields[count]
        time = fields[count+1]
        if validate_timestamp(date, time):
            bln_criterion_met = True
            fields.remove(date)
            fields.remove(time)
        elif count == len(fields) - 2:
            print('a')
            return None
        count += 1
        
    # Check there is a valid logging level given - we don't care where
    count = 0
    bln_criterion_met = False
    while not bln_criterion_met:
        if fields[count] in VALID_LOG_LEVELS:
            bln_criterion_met = True
            fields.remove(fields[count])
        elif count == len(fields) - 1:
            return None
        count += 1
        
    # Checks if there are fields other than timestamp and logging level before message
    if fields.count("") != len(fields):
        return None

    return True


# [TODO]: step 2
# Update the get_dict function below so it converts a line of the logs into a
# dictionary with keys for "timestamp", "log_level", and "message". The valid log
# levels are `INFO`, `TRACE`, and `WARNING`. See lines 67 to 71 for how we expect the
# results to look.
def get_dict(line):
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    message = " :".join(line.split(" :")[1:])
    pass


# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
