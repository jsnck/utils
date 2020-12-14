# -*- coding: utf-8 -*-
import json;
import re;
import csv;
import codecs;

#import json file (list)
with open('<input_path>') as file:
    data = json.load(file)

## uncomment if you want an id to every line, set start value of id here
#id = int
#id = 1

length = range(len(data))

#output .txt file
f = codecs.open('<output_path>', 'a', 'utf-8')

for i in length:
    current = data[i]
    for j in range(len(current['events'])):
        current_ev = current['events'][j]

        ##id uncomment if you want to add an id to every line, set start value of id above
        #f.write(str(id)+';')
        #id = id+1

        #sender_id
        f.write((json.dumps(current['sender_id'])+';').replace('"', ''))
        #type_name
        f.write((json.dumps(current['events'][j]['event'])+';').replace('"', ''))
        #timestamp
        f.write((json.dumps(current['events'][j]['timestamp'])+';').replace('"', ''))
        #intent_name
        if((current_ev.get('parse_data')) is not None):
            f.write((json.dumps(current['events'][j]['parse_data']['intent']['name'])+';').replace('"', ''))
            #f.write('Null;')
        else:
            f.write('Null;')
        #action_name
        if((current_ev.get('name')) is not None):
            f.write((json.dumps(current['events'][j]['name'])+';').replace('"', ''))
        else:
            f.write('Null;')
        #events
        f.write((json.dumps(current['events'][j])+'\n').replace('\\', '\\\\'))
f.close()