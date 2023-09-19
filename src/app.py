import sys
import argparse
import pdfkit 
from pyhtml2pdf import converter
from datetime import datetime
 
def printTime(startTime, enddate):     
    current_start_time = startTime.strftime("%H:%M:%S")
    current_end_time = enddate.strftime("%H:%M:%S")
    difTime = (enddate- startTime).seconds
    schema = {
        "start": current_start_time,
        "end": current_end_time,
        "dif": difTime
    }
    print(schema)

def convert_html_to_PDF(url, fileName):
    startTime = datetime.now()   
    try:        
        config = pdfkit.configuration()
        pdfkit.from_url(url, fileName, configuration=config)
    except:         
        print("error exec 'pdfkit.from_url' ") 
    endTime = datetime.now()    
    printTime(startTime, endTime)  

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("url", help="input the URL valid from download PDF",
                type=str)
        parser.add_argument("filename", help="input the file name valid to save PDF",
                type=str)
        args = parser.parse_args()        

        convert_html_to_PDF(args.url, args.filename)
    except:
        e = sys.exc_info()[0]
        print("error exec ", e)


