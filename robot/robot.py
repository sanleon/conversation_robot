import csv

csv_file_name = 'ranking.csv'

def recommend_restaurant_info():
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        sort_result = sorted(reader, key=lambda d: float(d['COUNT']))
        return sort_result

def read_from_csv(restaurant):
    with open(csv_file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        count_dic_list = []
        input_rest = ''
        for row in reader:
            name = row['NAME']
            if name == restaurant:
                input_rest = restaurant
                cnt = row['COUNT']
                row['COUNT'] = int(cnt) + 1
                # print(row['COUNT'])
            count_dic_list.append(row)
        if input_rest == '':
            new_row = {'NAME': restaurant, 'COUNT': 1}
            count_dic_list.append(new_row)
    return count_dic_list


def write_to_csv(count_list):
    with open(csv_file_name, 'w', newline='') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in count_list:
            writer.writerow(row)