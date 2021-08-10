# LATEST TOKEN TRANSFERS
import requests
import json
import pandas as pd

def run_query(query):  # A simple function to use requests.post to make the API call.
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


query = """
{
    ethereum(network: bsc){
        transfers(
            options: {desc: "block.timestamp.time", limit: 10, offset: 0}, 
            date: {since: "2021-08-10", till: null}, 
            amount: {gt: 0}, 
            currency: {is: "0x20de22029ab63cf9a7cf5feb2b737ca1ee4c82a6"}){
                block {
        timestamp {
          time(format: "%Y-%m-%d %H:%M:%S")
        }
        height
      }
      sender {
        address
        annotation
      }
      receiver {
        address
        annotation
      }
      transaction {
        hash
      }
      amount
      currency {
        symbol
      }
      external
            }
    }
}



"""

result = run_query(query)  # Execute the query
#print ('Result - {}'.format(result))
#print(type(result))
pd.json_normalize(result['data']['ethereum']['transfers'])

# SENDERS
import requests
import json
import pandas as pd

def run_query(query):  # A simple function to use requests.post to make the API call.
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


query = """
{
    ethereum(network: bsc){
    transfers(currency: {is: "0x20de22029ab63cf9a7cf5feb2b737ca1ee4c82a6"}
    date: {since: null till: null}
    height:{gt: 0}
    amount: {gt: 0}
    options: {desc: "amount", limit:10, offset: 0}
    ){

      sender {
        address
        annotation
      }
      currency {
        symbol
      }
      amount
      count
      receiver_count: count(uniq: receivers)
      max_amount: maximum(of: amount, get: amount)
      max_date:maximum(of: date)
    }
  }
}

"""

result = run_query(query)  # Execute the query
#print ('Result - {}'.format(result))
#print(type(result))
pd.json_normalize(result['data']['ethereum']['transfers'])

# RECEIVERS
import requests
import json
import pandas as pd

def run_query(query):  # A simple function to use requests.post to make the API call.
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


query = """
{
  ethereum(network: bsc){
    transfers(currency: {is: "0x20de22029ab63cf9a7cf5feb2b737ca1ee4c82a6"}
    date: {since: null till: null}
    height:{gt: 1}
    amount: {gt: 0}
    options: {desc: "amount", limit:10, offset: 0}
    ){

      receiver {
        address
        annotation
      }
      currency {
        symbol
      }
      amount
      count
      sender_count: count(uniq: senders)
      max_amount: maximum(of: amount, get: amount)
      max_date:maximum(of: date)
    }
  }
}

"""

result = run_query(query)  # Execute the query
#print ('Result - {}'.format(result))
#print(type(result))
pd.json_normalize(result['data']['ethereum']['transfers'])
