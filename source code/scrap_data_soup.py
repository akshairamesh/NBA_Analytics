from bs4 import BeautifulSoup
import requests
def parse_html_table(html_table):
    '''For parsing basketball reference stats html table.
    We will apply this function to every seasons html page.'''
    data = []
    cur_row = []
    row_names = []
    for ele in html_table:
        stat_name  = ele['data-stat']
        stat_value = ele.string
        new_row = (stat_name == 'player')
        if new_row:
            if cur_row:
                data.append(cur_row)
            cur_row = []
            col_names = []
            cur_row.append(ele['csk']) # fix asterisk error
            col_names.append(stat_name)
            continue
        cur_row.append(stat_value)
        col_names.append(stat_name)
    return data, col_names

