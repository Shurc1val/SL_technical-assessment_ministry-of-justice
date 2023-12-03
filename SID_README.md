## test_1.py
### step_1
I have defined a valid log line as one which contains a valid logging level and a valid timestamp (in either order), followed by a valid message (all separated at least a single space), with no other fields;

I have made the following assumptions about valid forms:
<ul>
    <li> A valid logging level matches one of the options given in the constant tuple VALID_LOG_LEVELS; </li>
    <li> A valid timestamp includes a date and time matching the formats given by the constant strings VALID_DATE_FORMAT and VALID_TIME_FORMAT respectively, in that order and separated by a single space; </li>
    <li> A valid message is a string starting with the character ":", and containing at least one other character that is not a space. </li>
</ul>

## test_3.py
I have assumed that when the task says the function "should sum all the numbers at the current time", it means to sum the three two-digit numbers (HH, MM, SS), rather than the six one-digit numbers (H,H,M,M,S,S).
I have also added an option to verify the inputs are valid time strings before converting to prevent the program from crashing; however, as I do not know the intended use of the function, this option is set off as default (for instance, the function may be intended to be wrapped in a try-except at a higher level, with a more appropriate error handling message / response).