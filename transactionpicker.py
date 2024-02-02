# Import Libraries
from flask import Flask, jsonify
from data import transactions_list
#from data import ten_highest_fees_list
#from data import ten_lowest_fees_list
#from data import next_highest_total_list


# Create Web App
app = Flask(__name__)


# returns list of transactions
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200




# Returns list of 10 transactions with highest fees
@app.route('/get_ten_highest_fees', methods=['GET'])
def get_ten_highest_fees():
    
    for i in range(0, len(transactions_list)-1):
        for j in range(0, len(transactions_list)-1):
            if transactions_list[j]['Fee'] > transactions_list[j+1]['Fee']:
                temp = transactions_list[j]
                transactions_list[j] = transactions_list[j+1]
                transactions_list[j+1] = temp
 
    ten_highest_fees_list = transactions_list[-10:]
    
    response = {'Ten highest fees': ten_highest_fees_list}
    return jsonify(response), 200




# Returns list of 10 transactions with lowest fees
@app.route('/get_ten_lowest_fees', methods=['GET'])
def get_ten_lowest_fees():
    
    for i in range(0, len(transactions_list)-1):
        for j in range(0, len(transactions_list)-1):
            if transactions_list[j]['Fee'] > transactions_list[j+1]['Fee']:
                temp = transactions_list[j]
                transactions_list[j] = transactions_list[j+1]
                transactions_list[j+1] = temp

    ten_lowest_fees_list = transactions_list[:10]
    
    response = {'Ten lowest fees': ten_lowest_fees_list}
    return jsonify(response), 200


    

# Returns second highest total fee sum after picking 10 xtransactions
@app.route('/get_next_highest_total', methods=['GET'])
def get_next_highest_total():
    
    for i in range(0, len(transactions_list)-1):
        for j in range(0, len(transactions_list)-1):
            if transactions_list[j]['Fee'] > transactions_list[j+1]['Fee']:
                temp = transactions_list[j]
                transactions_list[j] = transactions_list[j+1]
                transactions_list[j+1] = temp
 
    next_highest_total_list = transactions_list[-9:]
    eleventh_value = transactions_list[-11]['Fee']
    
    sum = 0
    for f in range(0,len(next_highest_total_list)):
        sum += f
        
    sum += eleventh_value
    return_val = str(sum)
    #response = {'Get next highest total': next_highest_total_list}

    return return_val
    #return jsonify(response), 200 
    #return jsonify(eleventh_value), 200


# Run app
app.run(host='0.0.0.0', port=5050)