from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
#import pandas as pd

import numpy as np
import pandas as pd
import math
import io
from datetime import datetime


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#from datetime import datetime

# In[30]:
def an():
    authcookie = Office365('https://apxnproperty.sharepoint.com', username='dev1@apxnproperty.com', password='DV@apxn365').GetCookies()
    site = Site('https://apxnproperty.sharepoint.com/sites/CountySelection', version=Version.v2016, authcookie=authcookie)
    #folder = site.Folder('apxn/CountyWise')
    #folder = site.Folder('apxn/Analysis')
    now = datetime.now()
    dt_string = now.strftime("%B")    
    
    #state = 'NV'
    #states=['AL','AZ','AR','CO','GA','ID','IN','KY','ME','MN','MS','MO','MT','NV','NH','NY','NC','OK','OR','SC','SD','TN','TX','UT','VT','WA','WI','WY']
    states=['AZ','FL','UT','NV','OR','NY']
    for state in states:
        state=state.lower()
        folder = site.Folder('apxn/Realtor')
        data=folder.get_file(dt_string+'_Realtor.csv')
        realtor=pd.read_csv(io.BytesIO(data),error_bad_lines=False,engine='python')

        folder=site.Folder('apxn/UsCensusData')
        data=folder.get_file('PopulationEstimates.xls')
        population=pd.read_excel(io.BytesIO(data),sheet_name = 'Population Estimates 2010-19', header = None)[2:]

        folder=site.Folder('apxn/UsCensusData')
        data=folder.get_file('UrbanInfluenceCodes2013.xls')
        uic=pd.read_excel(io.BytesIO(data))


        #DataTree_filename = 'Nevada Sold 2020.csv'
        #realtor_filename = 'RDC_Inventory_Core_Metrics_County (3).csv'
        #redfin_filename = 'Nevada Redfin 2020.xlsx'

        #weights for county ranking
        population_density = 1
        residents_per_property = 1
        domestic_migration_2019 = 4
        weighted_domestic_migration = 2
        days_on_market_realtor = 3
        days_on_market_redfin = 3
        days_on_market_average = 0
        new_list_to_sold = 1
        sold_to_total_properties = 3
        in_zip_owners = 2
        in_state_owners = 1

        export = 'yes' #export the data to excel
        sold_data = 'yes'

        # In[3]:


        #countywise = pd.read_html("https://countywise.com/" + state.lower() + '/', header = 0)[0]
        #realtor = pd.read_csv('C:\\Users\\Riley Chabot\\Downloads\\' + realtor_filename)
        realtor['county_fips'] = realtor['county_fips'].astype(str).str.zfill(5)
        #population = pd.read_excel(r'C:\Users\Riley Chabot\Downloads\PopulationEstimates.xls', sheet_name = 'Population Estimates 2010-19', header = None)[2:]
        header = population.iloc[0]
        population = population[1:]
        population.columns = header
        columns = population.columns[8:]
        for column in columns:
            population[column] = population[column].astype(float)
        #uic = pd.read_excel(r'C:\Users\Riley Chabot\Downloads\UrbanInfluenceCodes2013.xls', sheet_name = 'Urban Influence Codes 2013')
        for column in uic.columns:
            uic[column] = uic[column].astype(str)
        uic.FIPS = uic.FIPS.str.zfill(5)

        folder=site.Folder('apxn/UsCensusData')
        data=folder.get_file('RuralUrbanContinuum.xlsx')
        rucc=pd.read_excel(io.BytesIO(data))
        folder=site.Folder('apxn/Redfin')
        name=dt_string+"_Redfin_"+state+".xlsx"
        #data=folder.get_file('April_Redfin_nv.xlsx')
        data=folder.get_file(name)
        redfin=pd.read_excel(io.BytesIO(data))
        redfin.Region = redfin.Region.fillna('').astype(str)
        regions = []
        constant = ''
        for i, row in redfin.iterrows():
            place = row['Region']
            if place != '':
                constant = place
                regions.append(constant)
            else:
                regions.append(constant)
                
                
            
        redfin['Region'] = regions
        folder=site.Folder('apxn/ZipCodeData')
        data=folder.get_file('Zip Code Data.xlsx')
        zips=pd.read_excel(io.BytesIO(data))

        zips = zips[zips.state_id == state]
        zips.zip = zips.zip.astype(str).str.zfill(5)
        zips.county_fips = zips.county_fips.astype(str).str.zfill(5)
        folder=site.Folder('apxn/Datatree')
        #data=folder.get_file('Sold_nv.csv')
        name=dt_string+"_Sold_"+state+".csv"
        data=folder.get_file(name)
        sold_df=pd.read_csv(io.BytesIO(data))

        #sold_df = pd.read_csv('Nevada Sold 2020.csv')
        keepers = ['SITUS ZIP CODE', 'LATITUDE', 'LONGITUDE', 'MAIL STATE', 'MAIL ZIP/ZIP+4','COUNTY', 'FIPSCODE', 'APN - FORMATTED', 'ALTERNATE APN', 'LOT ACREAGE', 'ASSESSED TOTAL VALUE', 'ASSESSED LAND VALUE', 'LMS-SALE PRICE', 'PRIOR SALE PRICE', 'LINK']
        sold_df = sold_df[keepers]
        sold_df = sold_df.replace({'=':''}, regex=True)
        sold_df = sold_df.replace({',':''}, regex=True)
        sold_df = sold_df.replace({'\$':''}, regex=True)
        sold_df = sold_df.replace({'"':''}, regex=True)
        sold_df = sold_df.replace({'HYPERLINK':''}, regex=True)
        sold_df = sold_df.replace({'\(':''}, regex=True)
        sold_df = sold_df.replace({'\)':''}, regex=True)
        sold_df['MAIL ZIP/ZIP+4'] = sold_df['MAIL ZIP/ZIP+4'].str[:5]
        sold_df = sold_df.rename(columns = {'MAIL ZIP/ZIP+4': 'MAIL ZIP'})
        sold_df['COUNTY'] = sold_df['COUNTY'].str.upper()
        sold_df['FIPSCODE'] = sold_df['FIPSCODE'].astype(str).str.zfill(5)
        sold_df['ASSESSED TOTAL VALUE'] = sold_df['ASSESSED TOTAL VALUE'].astype(float)
        sold_df['ASSESSED LAND VALUE'] = sold_df['ASSESSED LAND VALUE'].astype(float)
        sold_df['LMS-SALE PRICE'] = sold_df['LMS-SALE PRICE'].astype(float)
        sold_df['PRIOR SALE PRICE'] = sold_df['PRIOR SALE PRICE'].astype(float)
        sold_df['SITUS ZIP CODE'] = sold_df['SITUS ZIP CODE'].astype(str)
            
        situs_zips = []
        for index, row in sold_df.iterrows():
            county = row.COUNTY
            zipcode = row['SITUS ZIP CODE']
            if (zipcode == 'nan' or zipcode == ''):
                p1 = np.array((row.LATITUDE, row.LONGITUDE))
                zipc = ''
                dist = 100000.00
                zips_temp = zips[zips.county_name.str.upper() == county.upper()]
                for i, r in zips_temp.iterrows():
                    p2 = np.array((r.lat, r.lng))
                    dist_new = np.linalg.norm(p1-p2)
                    if dist_new < dist:
                        dist = dist_new
                        zipc = r.zip
                situs_zips.append(zipc)
            else:
                situs_zips.append(zipcode)
        sold_df['SITUS ZIP CODE'] = situs_zips

        sold_df = sold_df[(sold_df['LMS-SALE PRICE'] != 0.0) & (sold_df['LOT ACREAGE'] != 0.0)]
        sold_df['Sale Price per Acre'] = sold_df['LMS-SALE PRICE'].div(sold_df['LOT ACREAGE'])
        sold_df = sold_df.round(2)

        #sold_df['SITUS ZIP CODE'] = situs_zips
        folder = site.Folder('apxn/CountyWise')
        #folder.upload_file('Hello', 'new.txt')
        #data=folder.get_file('April_CountyWise_nv.csv')
        name=dt_string+"_countywise_"+state+".csv"
        data=folder.get_file(name)
        countywise=pd.read_csv(io.BytesIO(data))
        header_row=0
        countywise.columns = countywise.iloc[header_row]

        for i,j in enumerate(countywise['# of properties*']):
            try:
                k=j.replace(",","")
                countywise.loc[i,"# of properties*"]=k
            except:
                pass

        #countywise["# of properties*"].astype('float')

        df = pd.DataFrame()
        fips = population[population.State == state].FIPStxt[1:]
        counties = population[population.State == state].Area_Name[1:]
        states = population[population.State == state].State[1:]

        df['FIPS'] = fips
        df['State'] = states
        df['County'] = counties
        df = pd.DataFrame()
        fips = population[population.State == state].FIPStxt[1:]
        counties = population[population.State == state].Area_Name[1:]
        states = population[population.State == state].State[1:]

        df['FIPS'] = fips
        df['State'] = states
        df['County'] = counties

        county_names = []
        realtor_doms = []
        realtor_al = []
        redfin_doms = []
        redfin_new_to_sold = []
        avg_doms = []
        migrations = []
        migs15 = []
        migs16 = []
        migs17 = []
        migs18 = []
        migs19 = []
        densities = []
        pops = []
        areas = []
        props = []
        per_props = []
        urbans = []
        udesc = []
        rurals = []
        rdesc = []
        econs = []
        edesc = []
        metros = []
        solds = []
        solds_per_prop = []
        in_zips = []
        in_states = []
        zips_percentage = []
        states_percentage = []
        mean_sale_prices = []
        median_sale_prices = []
        std_sale_prices = []
        mean_ppa = []
        median_ppa = []
        std_ppa = []
        mean_acres = []
        median_acres = []
        std_acres = []
        mean_sale_to_assessed = []
        median_sale_to_assessed = []
        std_sale_to_assessed = []



        for index, row in df.iterrows():
            county = row.County
            fips = row.FIPS
            
            countywise_bool = False
            if county[-6:] == 'County':
                new_county = county[:-7]
                countywise_bool = True
            else:
                new_county = county
                
            county_names.append(new_county)
            
            mig15 = population.loc[population.FIPStxt == fips, 'R_DOMESTIC_MIG_2015'].values[0]
            mig16 = population.loc[population.FIPStxt == fips, 'R_DOMESTIC_MIG_2016'].values[0]
            mig17 = population.loc[population.FIPStxt == fips, 'R_DOMESTIC_MIG_2017'].values[0]
            mig18 = population.loc[population.FIPStxt == fips, 'R_DOMESTIC_MIG_2018'].values[0]
            mig19 = population.loc[population.FIPStxt == fips, 'R_DOMESTIC_MIG_2019'].values[0]
            mig = .5*mig19 + .25*mig18 + .125*mig17 + .0625*mig16 + .0625*mig15
            migs15.append(mig15)
            migs16.append(mig16)
            migs17.append(mig17)
            migs18.append(mig18)
            migs19.append(mig19)
            migrations.append(mig)
            pop = population.loc[population.FIPStxt == fips, 'POP_ESTIMATE_2019'].values[0]
            pop=float(pop)
            pops.append(pop)
        

            urban = population.loc[population.FIPStxt == fips, 'Urban_Influence_Code_2013'].values[0]
            rural = population.loc[population.FIPStxt == fips, 'Rural-urban_Continuum Code_2013'].values[0]
            econ = population.loc[population.FIPStxt == fips, 'Economic_typology_2015'].values[0]
            urbans.append(urban)
            rurals.append(rural)
            econs.append(econ)
            udesc.append(uic.loc[uic.UIC_2013 == str(urban), 'Description'].values[0])
            rdesc.append(rucc.loc[rucc.Code == str(rural), 'Description'].values[0])
            if rural <=3:
                metros.append('Metro')
            else: 
                metros.append('Non-metro')
            
            if econ == 1:
                edesc.append('Farming')
            elif econ == 2:
                edesc.append('Mining')
            elif econ == 3:
                edesc.append('Manufacturing')
            elif econ == 4:
                edesc.append('Government')
            elif econ == 5:
                edesc.append('Recreation')
            elif econ == 0:
                edesc.append('Nonspecialized')
            
            if countywise_bool:
                area = countywise.loc[countywise['County / Parish / Borough'] == new_county, 'Square Miles*'].values[0]
                prop = countywise.loc[countywise['County / Parish / Borough'] == new_county, '# of properties*'].values[0]
                area=float(area)
                prop=float(prop)
            else:
                area = np.nan
                prop = np.nan
                
            areas.append(area)
            densities.append(pop/area)
            props.append(prop)
            per_props.append(pop/prop)
            
            
            realtor_bool = realtor['county_fips'].str.contains(fips).any()
            if realtor_bool:
                realtor_dom = realtor.loc[realtor.county_fips == fips, 'median_days_on_market'].values[0]
                realtor_doms.append(realtor_dom)
                realtor_al.append(realtor.loc[realtor.county_fips == fips, 'active_listing_count'].values[0])
            else:
                realtor_doms.append(np.nan)
                realtor_al.append(np.nan)
            
            redfin_bool = redfin['Region'].str.contains(county + ', ' + state).any()
            if redfin_bool:
                redfin_dom = redfin[redfin.Region == county + ', ' + state]['Days on Market'].mean()
                redfin_new_list = redfin[redfin.Region == county + ', ' + state]['New Listings'].sum()
                redfin_sold = redfin[redfin.Region == county + ', ' + state]['Homes Sold'].sum()
                redfin_new_to_sold.append(redfin_new_list/redfin_sold)
                redfin_doms.append(redfin_dom)
            else:
                redfin_doms.append(np.nan)
                redfin_new_to_sold.append(np.nan)
                
            if realtor_bool & redfin_bool:
                dom = (realtor_dom + redfin_dom)/2
            elif realtor_bool:
                dom = realtor_dom
            elif redfin_bool:
                dom = redfin_dom
            else:
                dom = np.nan
            avg_doms.append(dom)
            
            if sold_data == 'yes':
                sold_temp = sold_df[sold_df.FIPSCODE == fips]
                sold_num = len(sold_temp)
                solds.append(sold_num)
                if sold_num == 0:
                    solds_per_prop.append(0)
                else:
                    solds_per_prop.append(sold_num/prop)
                zip_num = 0
                state_num = 0
                for i, r in sold_temp.iterrows():
                    if r['SITUS ZIP CODE'] == r['MAIL ZIP']:
                        zip_num = zip_num + 1
                    if r['MAIL STATE'] == state:
                        state_num = state_num + 1
                in_zips.append(zip_num)
                in_states.append(state_num)
                if sold_num != 0:
                    zips_percentage.append((zip_num/sold_num)*100)
                    states_percentage.append((state_num/sold_num)*100)
                else:
                    zips_percentage.append(np.nan)
                    states_percentage.append(np.nan)
                mean_sale_prices.append(sold_temp['LMS-SALE PRICE'].mean())
                median_sale_prices.append(sold_temp['LMS-SALE PRICE'].median())
                std_sale_prices.append(sold_temp['LMS-SALE PRICE'].std())
                mean_ppa.append(sold_temp['Sale Price per Acre'].mean())
                median_ppa.append(sold_temp['Sale Price per Acre'].median())
                std_ppa.append(sold_temp['Sale Price per Acre'].std())
                mean_acres.append(sold_temp['LOT ACREAGE'].mean())
                median_acres.append(sold_temp['LOT ACREAGE'].median())
                std_acres.append(sold_temp['LOT ACREAGE'].std())
        #         mean_sale_to_assessed.append(sold_temp['Sale to Assessed Ratio'].mean())
        #         median_sale_to_assessed.append(sold_temp['Sale to Assessed Ratio'].median())
        #         std_sale_to_assessed.append(sold_temp['Sale to Assessed Ratio'].std())
                
            else:
                solds.append(np.nan)
                solds_per_prop.append(np.nan)
                in_zips.append(np.nan)
                in_states.append(np.nan)
                zips_percentage.append(np.nan)
                states_percentage.append(np.nan)
                mean_sale_prices.append(np.nan)
                median_sale_prices.append(np.nan)
                std_sale_prices.append(np.nan)
                mean_ppa.append(np.nan)
                median_ppa.append(np.nan)
                std_ppa.append(np.nan)
                mean_acres.append(np.nan)
                median_acres.append(np.nan)
                std_acres.append(np.nan)
                mean_sale_to_assessed.append(np.nan)
                median_sale_to_assessed.append(np.nan)
                std_sale_to_assessed.append(np.nan)

            

        df['County'] = county_names
        df['Population (2019)'] = pops
        df['Area (Sq. Miles)'] = areas
        df['Population Density'] = densities
        df['Metro?'] = metros
        df['Urban Influence Code (2013)'] = urbans
        df['UIC Description'] = udesc
        df['Rural-Urban Continuum Code (2013)'] = rurals
        df['RCC Description'] = rdesc
        df['Economic Typology (2015)'] = econs
        df['ET Description'] = edesc
        df['Domestic Migration 2015'] = migs15
        df['Domestic Migration 2016'] = migs16
        df['Domestic Migration 2017'] = migs17
        df['Domestic Migration 2018'] = migs18
        df['Domestic Migration 2019'] = migs19
        df['Weighted Domestic Migration'] = migrations
        df['Number of Properties'] = props
        df['Residents per Property'] = per_props
        df['Active Listings (Realtor)'] = realtor_al
        df['Days on Market (Realtor)'] = realtor_doms
        df['Days on Market (Redfin)'] = redfin_doms
        df['Avg. DOM'] = avg_doms
        df['New List to Sold'] = redfin_new_to_sold
        df['Recent Sold Properties'] = solds
        df['Recent Sold Properties to Total Properties'] = solds_per_prop
        df['Owners in-zip'] = in_zips
        df['Owners in-State'] = in_states
        df['Percent Owners in-zip'] = zips_percentage
        df['Percent Owners in-State'] = states_percentage
        df['Mean Sale Price'] = mean_sale_prices
        df['Median Sale Price'] = median_sale_prices
        df['Sale Price Std. Dev.'] = std_sale_prices
        df['Mean Sale Price per Acre'] = mean_ppa
        df['Median Sale Price per Acre'] = median_ppa
        df['Sale Price per Acre Std. Dev.'] = std_ppa
        df['Mean Lot Acreage'] = mean_acres
        df['Median Lot Acreage'] = median_acres
        df['Lot Acreage Std. Dev.'] = std_acres
        
    #df  

        df_normal = df[['Population Density', 'Residents per Property', 'Domestic Migration 2019', 'Weighted Domestic Migration', 'Days on Market (Realtor)', 'Days on Market (Redfin)', 'Avg. DOM', 'New List to Sold', 'Recent Sold Properties to Total Properties', 'Percent Owners in-zip', 'Percent Owners in-State']]
        df_mean = df_normal.mean(axis = 0)
        df_std = df_normal.std(axis = 0)
        df_normal = -1*(df_normal - df_mean)/df_std

        df_normal['Domestic Migration 2019'] *= -1
        df_normal['Weighted Domestic Migration'] *= -1
        df_normal['Recent Sold Properties to Total Properties'] *= -1

        df_normal.insert(0, 'FIPS', df.FIPS)
        df_normal.insert(1, 'State', df.State)
        df_normal.insert(2, 'County', df.County)

        rankings = pd.DataFrame()
        rankings['FIPS'] = df.FIPS
        rankings['State'] = df.State
        rankings['County'] = df.County
        #rankings.reset_index(inplace = True)
        rankings['Population Density Rank'] = df['Population Density'].rank(method = 'min')
        rankings['Residents per Property Rank'] = df['Residents per Property'].rank(method = 'min')
        rankings['Domestic Migration 2019 Rank'] = df['Domestic Migration 2019'].rank(method = 'min', ascending = False)
        rankings['Weighted Domestic Migration Rank'] = df['Weighted Domestic Migration'].rank(method = 'min', ascending = False)
        rankings['Days on Market (Realtor) Rank'] = df['Days on Market (Realtor)'].rank(method = 'min')
        rankings['Days on Market (Redfin) Rank'] = df['Days on Market (Redfin)'].rank(method = 'min')
        rankings['Days on Market (Combined) Rank'] = df['Avg. DOM'].rank(method = 'min')
        rankings['New List to Sold Rank'] = df['New List to Sold'].rank(method = 'min', ascending = False)
        rankings['Sold Properties to Total Properties Rank'] = df['Recent Sold Properties to Total Properties'].rank(method = 'min', ascending = False)
        rankings['In-zip Owners Rank'] = df['Percent Owners in-zip'].rank(method = 'min')
        rankings['In-State Owners Rank'] = df['Percent Owners in-State'].rank(method = 'min')
        rankings['Combined (Average)'] = rankings.mean(axis = 1)
        rankings['Combined (Average) Rank '] = rankings['Combined (Average)'].rank(method = 'min')
        rankings['Average Normal Score'] = df_normal.mean(axis = 1)
        rankings['Average Normal Score Rank'] = rankings['Average Normal Score'].rank(method = 'min', ascending = False)

        weights = [population_density, residents_per_property, domestic_migration_2019, weighted_domestic_migration, days_on_market_realtor, days_on_market_redfin, days_on_market_average, new_list_to_sold, sold_to_total_properties, in_zip_owners, in_state_owners]
        weighted_avg = []
        for index, row in rankings.iterrows():
            missing = 0
            value = 0
            var = []
            var.append(row['Population Density Rank'])
            var.append(row['Residents per Property Rank'])
            var.append(row['Domestic Migration 2019 Rank'])
            var.append(row['Weighted Domestic Migration Rank'])
            var.append(row['Days on Market (Realtor) Rank'])
            var.append(row['Days on Market (Redfin) Rank'])
            var.append(row['Days on Market (Combined) Rank'])
            var.append(row['New List to Sold Rank'])
            var.append(row['Sold Properties to Total Properties Rank'])
            var.append(row['In-zip Owners Rank'])
            var.append(row['In-State Owners Rank'])
            for i in range(len(var)):
                if math.isnan(var[i]):
                    missing = missing + weights[i]
                else:
                    value = value + var[i]*weights[i]
            weighted_avg.append(value/(sum(weights)-missing))
        rankings['Combined (Weighted Average)'] = weighted_avg
        rankings['Combined (Weighted Average) Rank'] = rankings['Combined (Weighted Average)'].rank(method = 'min')

        norm_weighted_avg = []
        for index, row in df_normal.iterrows():
            norm_missing = 0
            norm_value = 0
            norm_var = []
            norm_var.append(row['Population Density'])
            norm_var.append(row['Residents per Property'])
            norm_var.append(row['Domestic Migration 2019'])
            norm_var.append(row['Weighted Domestic Migration'])
            norm_var.append(row['Days on Market (Realtor)'])
            norm_var.append(row['Days on Market (Redfin)'])
            norm_var.append(row['Avg. DOM'])
            norm_var.append(row['New List to Sold'])
            norm_var.append(row['Recent Sold Properties to Total Properties'])
            norm_var.append(row['Percent Owners in-zip'])
            norm_var.append(row['Percent Owners in-State'])
            for i in range(len(norm_var)):
                if math.isnan(norm_var[i]):
                    norm_missing = norm_missing + weights[i]
                else:
                    norm_value = norm_value + norm_var[i]*weights[i]
            norm_weighted_avg.append(norm_value/(sum(weights)-norm_missing))
        rankings['Weighted Normal Score'] = norm_weighted_avg
        rankings['Weighted Normal Score Rank'] = rankings['Weighted Normal Score'].rank(method = 'min', ascending = False)


        summary = pd.DataFrame()

        summary['FIPS'] = df.FIPS
        summary['State'] = df.State
        summary['County'] = df.County
        summary['Population (2019)'] = df['Population (2019)']
        summary['Population Density'] = df['Population Density']
        summary['Number of Properties'] = df['Number of Properties'] 
        summary['Residents per Property'] = df['Residents per Property']
        summary['Days on Market (Realtor)'] = df['Days on Market (Realtor)']
        summary['Days on Market (Redfin)'] = df['Days on Market (Redfin)']
        summary['New List to Sold (Redfin)'] = df['New List to Sold']
        summary['Domestic Migration (2019)'] = df['Domestic Migration 2019']
        summary['Weighted Domestic Migration'] = df['Weighted Domestic Migration']
        summary['Recent Sold Properties'] = df['Recent Sold Properties']
        summary['Recent Sold to Total Properties'] = df['Recent Sold Properties to Total Properties']
        summary['Percent Owners in-zip'] = df['Percent Owners in-zip']
        summary['Percent Ownersin-State'] = df['Percent Owners in-State']
        summary['County Name'] = df.County
        summary['Average Ranking'] = rankings['Combined (Average)']
        summary['Normal Score Ranking'] = rankings['Average Normal Score Rank']
        summary['Urban Influence Code (2013)'] = df['Urban Influence Code (2013)']
        summary['UIC Description'] = df['UIC Description']
        summary['Rural-Urban Continuum Code'] = df['Rural-Urban Continuum Code (2013)']
        summary['RCC Description'] = df['RCC Description']



        #summary

        df.to_csv("Metrics.csv")
        summary.to_csv("Summary.csv")
        rankings.to_csv("Rankings.csv")
        filecon = open('Metrics.csv', 'rb')
        filecon1 = open('Summary.csv', 'rb')
        filecon2 = open('Rankings.csv', 'rb')
        now = datetime.now()
        from datetime import date
            
            
        now = datetime.now()

        print("now =", now)


        dt_string = now.strftime("%B")

        folder = site.Folder('apxn/Analysis')
        res=str(dt_string)+"_"+state+"_metrics"+".csv"
        res1=str(dt_string)+"_"+state+"_summary"+".csv"
        res2=str(dt_string)+"_"+state+"_ranking"+".csv"
        print(res)
        print(res1)
        print(res2)
        folder.upload_file(filecon, res)
        folder.upload_file(filecon1, res1)
        folder.upload_file(filecon2, res2)
an()