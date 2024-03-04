#Python
import json
 
def prepareResponse(event, msgText):
    response = {
          "sessionState": {
            "dialogAction": {
              "type": "Close"
            },
            "intent": {
              "name": event['sessionState']['intent']['name'],
                  "state": "Fulfilled"
            }
          },
          "messages": [
           {
             "contentType": "PlainText",
             "content": msgText
            }
           ]
       }
     
    return response
 
def cancelIceCreamOrder(event):
    # Your order cancelation code here
    msgText = "Order has been canceled"
    return prepareResponse(event, msgText)
 
def createIceCreamOrder(event):
      
     firstName = event['sessionState']['intent']['slots']['name']['value']['interpretedValue']
     iceCreamFlavor = event['sessionState']['intent']['slots']['flavor']['value']['interpretedValue']
     iceCreamSize = event['sessionState']['intent']['slots']['size']['value']['interpretedValue']
      
     print(firstName, iceCreamFlavor, iceCreamSize)
      
     discount = event['sessionState']['sessionAttributes']['discount']
      
     #print('Discount: ', discount)
      
     # Your custom order creation code here.
      
     msgText = "Your Order for, " + str(iceCreamSize) + " " + str(iceCreamFlavor) + " IceCream has been placed with Order#: 342342"
 
     return prepareResponse(event, msgText)   
      
     
def lambda_handler(event, context):
    intentName = event['sessionState']['intent']['name']
    response = None
         
    if intentName == 'CreateOrderIntent':
        response = createIceCreamOrder(event)
    elif intentName == 'CancelOrderIntent':
        response = cancelIceCreamOrder(event)
    else: 
        raise Exception('The intent : ' + intentName + ' is not supported')
    return response