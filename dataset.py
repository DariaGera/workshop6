import plotly
import plotly.graph_objs as go

from pprint import PrettyPrinter
pp = PrettyPrinter(width=1, indent=1)
print = pp.pprint

import csv

f = open('DatafinitiElectronicsProductsPricingData.csv', encoding='utf-8')
nn = open('data', 'w')

f.readline()
for line in csv.reader(f):
	d=[]
	for el in line:
		d.append(el)
	lst=d[13].split(',')[0]+', '+d[12].split(',')[0]+', '+d[21].split(',')[0]+', '+d[6].split(',')[0]+', '+d[25].split(',')[0]+', '+d[1].split(',')[0]+', '+d[2].split(',')[0]+'\n'
	nn.write(lst)

f.close()
nn.close()
#---------------------------------------------------------------------------------------------
def convert_2_dict(lst):
	if len(lst[0]) == 3:
		return {
			'weight': lst[0][0],
			'prices_amountMax': lst[0][1],
			'prices_amountMin': lst[0][2]
		}
	
	dataset = {}
	for linn in lst:
		key = linn[0]
		if key not in dataset:
			dataset[key]=[]
		dataset[key].append(linn[1:])
	for key in dataset:
		dataset[key] = convert_2_dict(dataset[key])
	return dataset
	
with open('data', encoding='utf-8') as dat:
    dat.readline()
    file = [[el.strip() for el in line.split(',')] for line in dat]
    result = convert_2_dict(file)
#print(result)
#---------------------------------------------------------------------		
categories=[]
quantity_of_cat=[]
for category in result:
    categories.append(category)
    counter=0
    for brand in result[category]:
        for name in result[category][brand]:
            for date in result[category][brand][name]:
                counter+=1
    quantity_of_cat.append(counter)
		
#----------------------------------------------------------------------
brands=[]
max_price=[]
for category in result:
	for brand in result[category]:
		brands.append(brand)
		comparer=0
		for name in result[category][brand]:
			for date in result[category][brand][name]:
				must_max=float(result[category][brand][name][date]['prices_amountMax'])
				if must_max > comparer:
					comparer = must_max
	max_price.append(comparer)
#------------------------------------------------------------------------		
dates=[]
prices=[]

for date in result["LCD TVs"]["Samsung"]["Samsung - 50 Class (49.5\" Diag.) - LED - 1080p - Smart - HDTV\""]:
            dates.append(date)

dates.sort()
for date in dates:
    min = float(result["LCD TVs"]["Samsung"]["Samsung - 50 Class (49.5\" Diag.) - LED - 1080p - Smart - HDTV\""][date]["prices_amountMin"])
    max = float(result["LCD TVs"]["Samsung"]["Samsung - 50 Class (49.5\" Diag.) - LED - 1080p - Smart - HDTV\""][date]["prices_amountMax"])
    prices.append((min + max) / 2)


figure = { "data" : [
        {
            "x": dates,
            "y": prices,
            "type": "scatter",
            "name": "chane_of_avg_price_for_LCD_TV_Samsung.html",
        },
        {
            "x": brands,
            "y": max_price,
            "type": "bar",
            "name": "max_price_for_brand.html",
            "xaxis": "x2",
            "yaxis": "y2"
        },
        {
            "labels": categories,
            "values": quantity_of_cat,
            "type": "pie",
            "name": "quantity_of_categories.html",
            "textinfo": "none",
            'domain': {'x': [0, 0.45], 'y': [0.55, 1]},
        }
    ], "layout" : go.Layout(
            xaxis=dict(domain=[0, 0.45]), yaxis=dict(domain=[0, 0.45]),
            xaxis2=dict(domain=[0.55, 1]), yaxis2=dict(domain=[0, 0.45], anchor='x2'))}

plotly.offline.plot(figure,filename="workshop6.html")	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
