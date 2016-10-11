def main(photo, desired_size):
    print "--Photo Validity Checker--"
    valid = True
    log_string = unicode(photo.width) + "x" + unicode(photo.height) + ". Minimum desired size is: " + unicode(desired_size[0]) + "x" + unicode(desired_size[1]) 
    if desired_size[0] > photo.width:
        valid = False
    if desired_size[1] > photo.height:
        valid = False
    if valid:
        print "Photo size valid, resolution is: " + log_string
        return True
    else:
        print "Photo size NOT Valid, resolution is: " + log_string
        return False

if __name__ == "__main__":
     main()