import os
from flask import Flask, json, request, jsonify
# from models import insert_defect, find_defects
from datetime import date, datetime

app = Flask(__name__)

@app.route('/api/defects', methods=['GET'])
def get_defects():
    try:
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        defect_type = request.args.get('defectType')
        
        filters = {}
        
        if start_date and end_date:
            filters['date'] = {
                '$gte': datetime.strptime(start_date, "%Y-%m-%d"),
                '$lte': datetime.strptime(end_date, "%Y-%m-%d")
            }
        
        if defect_type:
            filters['defectType'] = defect_type
        
        # defects = find_defects(filters)
        defects = [
            {
                "defectType": "crack",
                "date": "2024-08-10",
                "description": "Crack on the surface",
                "severity": "high",
            }
        ]
        
        # f = open('/app/items_and_defects_data.json')
        # filename = os.path.join(app.static_folder, 'data', 'items_and_defects_data.json')
        # f = open(filename)

        # with open(filename) as test_file:
        #     data = json.load(test_file)

        # # returns JSON object as 
        # # a dictionary
        # data = json.load(filename)

        # Iterating through the json
        # list
        # for i in data['emp_details']:
        #     print(i)

        # Closing file
        # f.close()
        json_data = open(os.path.join(app.static_folder, "data", "items_and_defects_data.json"), "r")

        return json_data
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/defects', methods=['POST'])
def create_defect():
    try:
        data = request.json
        defect_type = data['defectType']
        date = data['date']
        description = data.get('description')
        severity = data.get('severity')
        
        # insert_defect(defect_type, date, description, severity)
        return jsonify({"message": "Defect created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()
