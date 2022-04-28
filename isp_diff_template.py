"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1,line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

s      Returns IDENTICAL if the two lines are the same.
    """
    
    
    if line1==line2:
        return IDENTICAL
    else:
        short_len = min(len(line1),len(line2))
        for index in range(short_len):
            if line1[index]!=line2[index]:
                return index
       
        return short_len
    
# line1='AAX'
# line2='AAA'
# print(singleline_diff(line1,line2))
#print(singleline_diff('Python i  fun!', 'Python is fun!!!'))       
#print (singleline_diff('', '') )

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if idx>len(line1) or idx>len(line2) or idx<0:
        return ""
    elif line1.find("\n")!=-1 or line1.find("\r")!=-1:
        return ""
    elif line2.find("\n")!=-1 or line2.find("\r")!=-1:
        return ""
    else:
        return line1 + "\n" + "="*idx + "^\n" + line2 + "\n"

# line1="abcd"
# line2="abcde"
# idx=4
# print(singleline_diff_format(line1,line2,idx))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    total_short_line = min(len(lines1),len(lines2))
    for line in range(total_short_line):
        index = singleline_diff(lines1[line],lines2[line])
        if index != IDENTICAL:
            return (line,index)
    if len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)
    else:
        return(total_short_line,0)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open (filename,"r") as open_file:
        file_list = open_file.read().splitlines()
    return file_list
    
#print(get_file_lines("file1.txt"))



def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    diff = multiline_diff(lines1,lines2)
    if diff == (IDENTICAL,IDENTICAL):
        return "No differences\n"
    
    else:
        if lines1 == []:
            return "Line1:\n\n^\n" + lines2[diff[0]] + "\n"
        elif lines2 == []:
            return "Line 0:\n" + lines1[diff[0]] + "\n^\n\n"
                                            
        else:
            return "Line " + str(diff[0]) + ":\n" + \
        singleline_diff_format(lines1[diff[0]], lines2[diff[0]],diff[1])
        
        
    
    
#print(file_diff_format('file8.txt', 'file9.txt') )