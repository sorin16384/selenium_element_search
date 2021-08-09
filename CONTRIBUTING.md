# Welcome  :smile:

If you wish to join me in making this script better, have a read at it, it's quite small for now, and see if you have any ideas, go for it and we'll see from there.

I'm quite bad at docstrings, so that's always something I could use help with.

Have you seen a typo?

Do you have an ideea how to make the code more readable, I'm open to suggestion!

New features and functionality? All ears (and eyes if I see a pull request)

Any contribution would be awesome, even if it's just an advice!!!

A thing that I need help with would be not to make a compleate mess with all this git branches, commits, pull requests and merges 😆

## Thank You :hugs:


Continuing, here is an example of the style used for writing docstrings for functions. I choosed this style by some trial and error so that when the mouse is hoovered over the function, at least in Spyder, Pycharm and when used with the .__doc__  attribute it dispalys well and as readable as possible in all three places (any news from other IDEs are welcome)

    
    def log_event(event, logfile='log.txt'):
        """
        Parameters:
            event (str): what should be logged

            logfile (str): (optional) the name(and path) of the log file ( default: 'log.txt')

        Returns:
                bool : True if everything went ok, False if something went wrong (such as creating file or writing to it)

        This function will write an event (what happened) to a file with timestamp, while also printing in the terminal what
        is being written.\n
        The function will write in the specified logfile, otherwise will create and/or write to a generic default log.txt file. Obviously
        any extension can be used (e.g.   .log,  .md,   .you_name_it)


        Usage Example: \n
        log_event('clicked login button', 'log_amazon_dot_com.txt')
        """
