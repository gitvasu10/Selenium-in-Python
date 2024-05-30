import logging

#   Timestamp: Type: <testcase name > : Message
def test_logging_demo():
     #getting an object for logging feature
    logger = logging.getLogger(__name__) #__name__ captures the current file name to be printed in the log file

    #File location, which comes from parent logging not the logger
    file_handler = logging.FileHandler("logfile.log")

    #Providing the format in which the output should be printed
    # %() ---> So that it can be evaluated at run time
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

    #Setting up the connection between the file and the logger
    file_handler.setFormatter(formatter)

    #The logger should also know where to write the logs in and save it
    logger.addHandler(file_handler) #Pass filehandler object to it


    #TYPES OF LOG(Logger Levels) --->
    # Debug
    # Info
    # Error
    # Warning
    # Critical

    #WHATEVER IS IN THE MESSAGE WILL BE PASSED INTO THE message VARIABLE AND THE LOGGER LEVER IN THE levelname RESPECTIVELY
    logger.setLevel(logging.INFO) # All statements but DEBUG will be printed
    logger.debug("This is my first debug code!")

    logger.info("Information statement not related to the errors and failures")

    logger.warning("The current version of the method is depricated...")

    logger.error("The test got failed")

    logger.critical("Update the method used in the script or the code breaks")

#Calling the function
test_logging_demo()
