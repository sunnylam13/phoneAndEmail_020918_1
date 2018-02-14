# Phone and Email Extraction from Clipboard

## PHONE REGEX

The phone number begins with an optional area code, so the area code group is followed with a question mark. 

Since the area code can be just three digits (that is, `\d{3}`) or three digits within parentheses (that is, `\(\d{3}\)`), you should have a pipe joining those parts. You can add the regex comment # Area code to this part of the multiline string to help you remember what `(\d{3}|\(\d{3}\))?` is supposed to match.

The phone number separator character can be a space (\s), hyphen (-), or period (.), so these parts should also be joined by pipes. 

The next few parts of the regular expression are straightforward: three digits, followed by another separator, followed by four digits. 

The last part is an optional extension made up of any number of spaces followed by ext, x, or ext., followed by two to five digits.

## EMAIL REGEX

The username part of the email address ➊ is one or more characters that can be any of the following: lowercase and uppercase letters, numbers, a dot, an underscore, a percent sign, a plus sign, or a hyphen. You can put all of these into a character class


The domain and username are separated by an @ symbol ➋. 

The domain name ➌ has a slightly less permissive character class with only letters, numbers, periods, and hyphens: [a-zA-Z0-9.-]. 

And last will be the "dot-com" part (technically known as the top-level domain), which can really be dot-anything. 
This is between two and four characters.

The format for email addresses has a lot of weird rules. This regular expression won’t match every possible valid email address, but it’ll match almost any typical email address you’ll encounter.

## FIND MATCHES IN CLIPPED TEXT

Now that you have specified the regular expressions for phone numbers and email addresses, you can let Python’s re module do the hard work of finding all the matches on the clipboard. 

The pyperclip.paste() function will get a string value of the text on the clipboard, and the findall() regex method will return a list of tuples.

one tuple (i.e. ('415','555','1842')) for each match 
and each tuple has strings for each group in the regex
REMEMBER:  group 0 matches the entire regex, so the group at index 0 of the tuple is the one you're interested in...
As you can see at ➊, you’ll store the matches in a list variable named matches. It starts off as an empty list, and a couple for loops. 

For the email addresses, you append group 0 of each match ➌. For the matched phone numbers, you don’t want to just append group 0. 

While the program detects phone numbers in several formats, you want the phone number appended to be in a single, standard format. 

The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text ➋. (These groups are the area code, first three digits, last four digits, and extension.)

## COPY RESULTS TO CLIPBOARD

The pyperclip.copy() function takes only a single string value, not a list of strings, so you call the join() method on matches.

To make it easier to see that the program is working, let’s print any matches you find to the terminal. And if no phone numbers or email addresses were found, the program should tell the user this.

