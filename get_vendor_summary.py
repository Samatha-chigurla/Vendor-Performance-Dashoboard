import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s,-%(levelname)s,-%(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
 '''this function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data'''
 vendor_sales_summary = pd.read_sql_query(""" WITH FreightSummary AS(
 select 
 VendorNumber,
 SUM(Freight) AS FreightCost
 From vendor_invoice
 group by VendorNumber
 ),


purchaseSummary as(
select
p.VendorNumber,
p.VendorName,
p.brand,
p.Description,
p.PurchasePrice,
pp.price as ActualPrice,
pp.Volume,
sum(p.Quantity) as TotalPurchaseQuantity,
sum(p.Dollars) as totalPurchaseDollars
from Purchases p
join Purchase_prices pp
on p.Brand = pp.Brand
where p.PurchasePrice >0 
group by p.VendorNumber, p.vendorname, p.Description, p.PurchasePrice, pp.Price, pp.Volume
),
 SalesSummary as(
 select
 VendorNo,
 Brand,
 sum(salesQuantity) as TotalSalesQuantity,
 sum(SalesDollars) as TotalsalesDollars,
 sum(SalesPrice) as TotalSalesPrice,
 sum(ExciseTax) as TotalExciseTax
 from sales
 group by VendorNo,Brand
 )

select
ps.vendorNumber,
ps.VendorName,
ps.Brand,
ps.Description,
ps.Purchaseprice,
Ps.ActualPrice,
ps.Volume,
ps.TotalPurchaseQuantity,
ps.TotalPurchaseDollars,
ss.TotalSalesQuantity,
ss.TotalSalesDollars,
ss.TotalSalesPrice,
ss.TotalExciseTax,
fs.FreightCost
from PurchaseSummary ps
left join SalesSummary ss
on ps.VendorNumber = ss.VendorNo
AND ps.Brand = ss.Brand
left JOin FreightSummary fs
on ps.VendorNumber = fs.VendorNumber
order by ps.TotalPurchasedollars DESC
""",conn)
 return vendor_sales_summary


def clean_data(df):
 '''this function will clean the data'''
 # changing datatype to float
 df['Volume'] = df['Volume'].astype('float')

 #filling missing value with 0
 df.fillna(0,inplace = True)

 #removing spaces from categorical columns
 df['VendorName'] = df['VendorName'].str.strip()
 df['Description'] = df['Description'].str.strip()

 #creating new columns for better analysis
 df['GrossProfit'] = df['TotalsalesDollars'] - df['totalPurchaseDollars']
 df['ProfitMargin'] = (df['GrossProfit'] / df['TotalsalesDollars']) * 100
 df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
 df['SalesToPurchaseRatio'] = df['TotalsalesDollars'] / df['totalPurchaseDollars']

 #vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalsalesDollars'] - vendor_sales_summary['totalPurchaseDollars']
 #vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit']/vendor_sales_summary['TotalsalesDollars'])*100
 #vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalSalesQuantity']/vendor_sales_summary['TotalPurchaseQuantity']
 #vendor_sales_summary['SalesToPurchaseRatio'] = vendor_sales_summary['TotalsalesDollars']/vendor_sales_summary['totalPurchaseDollars']



 return df
 #creatiing database connection
if __name__  == '__main__':
  conn = sqlite3.connect('inventory.db')

  logging.info('Creating Vendor summary Table.....')
  summary_df = create_vendor_summary(conn)
  logging.info(summary_df.head)

  logging.info("cleaning data.....")
  clean_df = clean_data(summary_df)
  logging.info(clean_df.head())

  logging.info('Ingesting Data...')
  ingest_db(clean_df,'vendor_sales_summary',conn)
  logging.info('completed')





