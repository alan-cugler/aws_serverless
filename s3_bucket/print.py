def lambda_handler(event, context):
    listSupport = event
    textSupport = listSupport[0]
    numSupport = listSupport[1]
    print(textSupport + " I've ran over " + str(numSupport) + " tests today alone!")
    return
