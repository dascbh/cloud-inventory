# -*- coding: utf-8 -*-

from json2html import *

data = {
		"i-0233dda6bd61c2f82": {
		"Owner": "Mauricio Aurelio",
		"Tags": {"App": "Autobots", "Ambiente": "PRJ", "Centro de Custo": "TI", "Gerencia": "Luciano Costa" },
		"Status": "Stopped",
		"Monthly Cost": "U$ 120",
		"Instance Type": "m5.xlarge", 
		"Reserved": "Yes"
	},
		"i-0237dda6bd39c9f73": {
		"Owner": "Juliana Castro",
		"Tags": {"App": "Autobots", "Ambiente": "PRJ", "Centro de Custo": "TI", "Gerencia": "Cristiano Silva" },
		"Status": "Running",
		"Monthly Cost": "220",
		"Instance Type": "m5.xlarge", 
		"Reserved": "No"
	},
		"i-0239dda6bd22c9f74": {
		"Owner": "Jessica Silva",
		"Tags": {"App": "Autobots", "Ambiente": "PRJ", "Centro de Custo": "TI", "Gerencia": "Thiago Barros" },
		"Status": "Running",
		"Monthly Cost": "220",
		"Instance Type": "m5.xlarge", 
		"Reserved": "No"
	}
}

def create_html(data):
	dyntable = json2html.convert(json = data, table_attributes="id=\"info-table\" class=\"table table-condensed table-bordered table-hover\"")

	strTable = '<html><link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">%s</html>' % (dyntable)

	hs = open("index.html", 'w')
	hs.write(strTable)
	 
	# print strTable

def main(data):
	create_html(data)

if __name__ == "__main__":
	main()