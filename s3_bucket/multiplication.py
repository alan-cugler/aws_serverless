def lambda_handler(event, context):
    listSupport = event
    numSupport = listSupport[1]
    numSupport = numSupport*10
    listSupport[1] = numSupport
    return listSupport
