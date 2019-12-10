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
	dyntable = json2html.convert(json = data, table_attributes="id=\"info-table\" class=\"table table-bordered\"")

	# Read the template file
	with open('template.html', 'r') as file:
		template = file.read()

	index = template.replace('*TABLE*', dyntable)

	# Write the new file
	with open('index.html', 'w') as file:
		file.write(index)

	return

def main(data):
	create_html(data)

if __name__ == "__main__":
	main()