import os
from flask import Flask, json, request, jsonify
from datetime import date, datetime
from enum import Enum
class ProductTypes(Enum):
    iphone = 'iphone'
    ipad = 'ipad'
    imac = 'imac'
    
class DefectTypes(Enum):
    damaged = 'Damaged'
    cracked = 'Cracked'
    deformed = 'Deformed'
    none = 'none'

base_cost = 600
maximum_cost_saving = 200
maximum_faulty_product = 25

app = Flask(__name__)

# Get defect production overview by product type, date range and product category
@app.route('/api/defects', methods=['GET'])
def get_defects():
    try:
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        defect_type = request.args.get('defectType')
        product_type = request.args.get('type')
        filtered_array = []
        with open(os.path.join(app.static_folder, "data", "items_and_defects_data.json"), "r") as io_str:
            data = json.load(io_str)
            filtered_array = data["data"]
            
            # Search By Date Range
            if start_date and end_date:
                filter_start_date = datetime.strptime(start_date, "%Y-%m-%d")
                filter_end_date = datetime.strptime(end_date, "%Y-%m-%d")
                filtered_array = [x for x in filtered_array if filter_start_date < datetime.strptime(x['date'], '%Y-%m-%d') and filter_end_date > datetime.strptime(x['date'], '%Y-%m-%d')]

            # Search By Product Category
            if product_type:
                filtered_array = [x for x in filtered_array if x['productCategory'] == product_type]
            
            # Search By Defect Type
            if defect_type:
                filtered_array = [x for x in filtered_array if x['defectType'] == defect_type]
    
        return filtered_array
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Get defect production overview by product type
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        product_overview = {}
        filtered_array = []
        with open(os.path.join(app.static_folder, "data", "items_and_defects_data.json"), "r") as io_str:
            output_dict = json.load(io_str)
            filtered_array = output_dict["data"]
            
            # Search By Date Range
            if start_date and end_date:
                filter_start_date = datetime.strptime(start_date, "%Y-%m-%d")
                filter_end_date = datetime.strptime(end_date, "%Y-%m-%d")
                filtered_array = [x for x in filtered_array if filter_start_date < datetime.strptime(x['date'], '%Y-%m-%d') and filter_end_date > datetime.strptime(x['date'], '%Y-%m-%d')]
            
            # Get product info by category
            for prod_type in ProductTypes:
                filteredProduct = []
                category_array = [x for x in filtered_array if x['productCategory'] == prod_type.name]
                
                # Get product info by defect types for pie charts
                for defectType in DefectTypes:
                    prod_stats = {}
                    category_defect_array = [x for x in category_array if x['defectType'] == defectType.name]
                    prod_stats['label'] = defectType.value
                    prod_stats['value'] = sum(item['faulty'] for item in category_defect_array)
                    filteredProduct.append(prod_stats)
                product_overview[prod_type.name] = filteredProduct
                    
        return product_overview
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get manfacturing stats by data
@app.route('/api/get_stats', methods=['GET'])
def get_stats():
    try:
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        defect_type = request.args.get('defectType')
        product_type = request.args.get('type')
        product_overview = {}
        filtered_array = []
        with open(os.path.join(app.static_folder, "data", "items_and_defects_data.json"), "r") as io_str:
            output_dict = json.load(io_str)
            filtered_array = output_dict["data"]
            
            # Search By Date Range
            if start_date and end_date:
                filter_start_date = datetime.strptime(start_date, "%Y-%m-%d")
                filter_end_date = datetime.strptime(end_date, "%Y-%m-%d")
                filtered_array = [x for x in filtered_array if filter_start_date < datetime.strptime(x['date'], '%Y-%m-%d') and filter_end_date > datetime.strptime(x['date'], '%Y-%m-%d')]
            
            # Search By Product Category
            if product_type:
                filtered_array = [x for x in filtered_array if x['productCategory'] == product_type]
            
            # Search By Defect Type
            if defect_type:
                filtered_array = [x for x in filtered_array if x['defectType'] == defect_type]
            
            avg_failure = 0
            max_failure = 0
            avg_cost_saving = 0
            min_cost_saving = 0
            avg_quality_score = 0
            max_quality_score = 0
            avg_product_efficiency = 0
            max_product_efficiency = 0
                
            for item in filtered_array:
                # Calculate Failure Rate
                if max_failure < item['faulty']:
                    max_failure = item['faulty']
                # if min_failure > item['faulty']:
                #     min_failure = item['faulty']
                
                avg_failure = avg_failure + item['faulty']
                
                # Calculate Cost Saving
                diff_cost = base_cost - item['cost']
                # if max_failure < diff_cost:
                #     max_failure = item['faulty']
                if min_cost_saving > diff_cost:
                    min_cost_saving = diff_cost
                
                avg_cost_saving = avg_cost_saving + diff_cost
                
                # Calculate Quality Score
                diff_quality_score = item['total_units'] - item['faulty']
                
                if max_quality_score < diff_quality_score:
                    max_quality_score= diff_quality_score
                
                avg_quality_score = avg_quality_score + diff_quality_score
                
                # Calculate Product Efficiency
                diff_product_efficiency = maximum_faulty_product - item['faulty']                
                if max_product_efficiency < diff_product_efficiency:
                    max_product_efficiency = diff_product_efficiency
                    
                avg_product_efficiency = avg_product_efficiency + diff_product_efficiency
                
            arr_length = len(filtered_array) if len(filtered_array) > 0 else 1
            print("arr_length")
            print(arr_length)
            product_overview['failure_rate'] = round(avg_failure / arr_length, 2)
            product_overview['failure_rate_trend'] = round((max_failure - avg_failure) / maximum_faulty_product, 2)
            product_overview['cost_saving'] = round(((avg_cost_saving / arr_length) * 100) / maximum_cost_saving, 2)
            product_overview['cost_saving_trend'] = round(((base_cost - min_cost_saving) / base_cost), 2)
            product_overview['quality_score'] = round(avg_quality_score / arr_length, 2)
            product_overview['quality_score_trend'] = round((max_quality_score - (avg_cost_saving / arr_length)) / 100, 2)
            product_overview['product_efficiency'] = round(avg_product_efficiency / arr_length, 2)
            product_overview['product_efficiency_trend'] = round(max_product_efficiency - (avg_product_efficiency / arr_length), 2)
                    
            return product_overview
    
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
