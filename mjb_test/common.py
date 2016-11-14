import sys

def prompt_and_confirm(prompt='Would you like to continue?', response = '', confirm_message='', choices={'y':True, 'Y':True, 'n':False, 'N':False}, skip=False, exit_on_false=False):
  try:
    if skip == False:
      valid_choices = choices.keys()
      while response.strip() not in valid_choices:
        response = raw_input('\033[1m{0} [{1}]: \033[0m'.format(prompt, '|'.join(valid_choices)))
        if response.strip() not in valid_choices:
          print 'Invalid response!'
      if choices[response] == False:
        if exit_on_false:
          print 'Exiting.'
          sys.exit(0)
        else:
          return False
    print confirm_message
    return True
  except KeyboardInterrupt:
    print "\nExiting."
    sys.exit(0)
