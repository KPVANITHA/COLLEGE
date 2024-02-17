import math

f = open("/content/PlayTennis.csv", "r")
tempData = f.readlines()
data = []

def calcInfoGain(feature_data):
    tot_p = 0
    tot_n = 0
    tot_count = 0
    for ele in feature_data:
        tot_count += len(feature_data[ele])
    temp_info = 0
    for value in feature_data:
        current_value = feature_data[value]
        pos_count = current_value.count("yes")
        neg_count = current_value.count("no")
        tot_p += pos_count
        tot_n += neg_count
        if (pos_count == 0 or neg_count == 0):
            continue
        elif (pos_count == neg_count):
            temp_info += (len(current_value) / tot_count)
            continue
        info = -(pos_count / len(current_value) * math.log2(pos_count / len(current_value))) - (neg_count / len(current_value) * math.log2(neg_count / len(current_value)))
        print("info for ", value, " : ", info)
        temp_info += (len(current_value) / tot_count) * info
    entropy = -((tot_p / tot_count) * math.log2(max(tot_p / tot_count, 0.00001))) - ((tot_n / tot_count) * math.log2(max(tot_n / tot_count, 0.00001)))
    
    #entropy = -((tot_p / tot_count) * math.log2(tot_p / tot_count)) - ((tot_n / tot_count) * math.log2(tot_n / tot_count))
    info_gain = entropy - temp_info
    return info_gain


# prepare data

features_list = tempData[0].split(",")
features_list = features_list[:-1]

for i in range(1, len(tempData)):
    temp = tempData[i].split(",")
    temp[-1] = temp[-1][:-1]
    data.append(temp)

processed_data = {}

for i in range(len(features_list)):
    current_feature = features_list[i]
    unique_values = {}
    for ele in data:
        if ele[i] not in unique_values:
            unique_values[ele[i]] = [ele[-1]]
        else:
            unique_values[ele[i]].append(ele[-1])
    processed_data[current_feature] = unique_values

print(processed_data)

info = {}

for feature in processed_data:
    current_feature_data = processed_data[feature]
    info_gain = calcInfoGain(current_feature_data)
    info[feature] = info_gain

max_entropy = -10
max_feature = None
for ele in info:
    if (info[ele] > max_entropy):
        max_entropy = info[ele]
        max_feature = ele

print(info)
print("Root node of decision tree : ", max_feature)
# Print the child nodes of the root node

print("Child nodes of root node :")
for value in processed_data[max_feature]:
    print(value)
