from bs4 import BeautifulSoup
import requests
import re
import time
from tqdm import tqdm
from html_table_extractor.extractor import Extractor
from pprint import pprint



def get_sanity_check(page, status):
    if status == True:
        completed_pages = open("completed_pages.txt","a+")
        completed_pages.write(str(page)+"\n")
    else:
        error_pages = open("error_pages.txt", "a+")
        error_pages.write(str(page)+"\n")



def get_table(endd_url):
    """
    end_url : "searching_list_brands.php?comp_id=&brand_id=83794&gen_mask=,1494,1524,&qty=1494@1000 TCID50~1524@1000 TCID50&gcount=2','','scrollbars=yes,width=800,height=600"

    :param endd_url:
    :return:
    """
    url = "http://www.medguideindia.com/"+str(endd_url)
    # print("Final Url : ", url)
    r = requests.get(url)
    out_file = open("out.csv", "a+")

    soup = BeautifulSoup(r.text)
    tab = soup.findAll("table")
    extractor = Extractor(tab[-1])
    extractor.parse()
    table_content = extractor.return_list()
    for row in table_content:
        line = "ж".join([str(each_cell).strip().replace('\n',"").replace("  "," ") for each_cell in row] )
        out_file.write(str(line) + "\n")
    out_file.flush()


def redirect_to_faltupage(brandid):
    url = "http://www.medguideindia.com/"+str(brandid)
    r = requests.get(url)
    data = r.text
    # apply regex to get brand_id
    try:
        endd_url = re.findall(r"\'(searching_list(_similar)?_brands.php?.*')\)", data)
        if endd_url ==[]:
            return False
        return str(endd_url[0][0])
    except:
        return False

def return_page(page_no):
    page_no = str(page_no)
    url = "http://www.medguideindia.com/show_brand.php?nav_link=&pageNum_rr="+page_no+"&nav_link=&selectme="+page_no
    r = requests.get(url)
    data = r.text
    # apply regex to get brand_id
    found_brand_ids = re.findall(r"mypopup_41\('(.*)'\)", data)
    if found_brand_ids:
        return found_brand_ids
    else:
        return None

def main():
    brand_ids_file = open("brand_ids","a+")

    brand_ids_accumlator = brand_ids_file.read().splitlines()
    for page in ["213","107","661","761","1026","1145","1347","1458","1537","1586","1593","1616","1677","2023"]:
        brand_ids = return_page(page)

        try:
            if brand_ids and (brand_ids not in brand_ids_accumlator):
                brand_ids_accumlator.extend(brand_ids)
                for each_id in brand_ids:
                    # print("#############################################################")
                    # print("id: ", each_id)
                    end_url = redirect_to_faltupage(each_id)
                    # print("end_url : ",end_url)
                    if end_url != False:
                        get_table(end_url)
                    #     print("Table Extracted")
                    # print("#############################################################")
            get_sanity_check(page,True)
        except:
            for i in brand_ids_accumlator:
                brand_ids_file.write(str(i)+"\n")
            get_sanity_check(page, False)
main()



