contaminated_nov = [28024,8142,16714,155319,123073,30650,119780,51684,407791,29806,4713,23777,15733,167516,54320,21475,63686,103441,23808,6510,145592]
healed_nov = [8939,1797,5449,49119,45586,15297,27212,37081,260528,10626,1875,11924,12631,86334,14065,7503,21507,58774,15166,4878,61216]
deaths_nov = [893,153,295,1673,5753,838,2367,2387,21855,1264,118,531,654,6239,1483,444,1555,2641,407,315,3711]
regions = ['Abruzzo','Basilicata','Calabria','Campania','Emilia-Romagna','Friuli Venezia Giulia','Lazio','Liguria','Lombardia','Marche','Molise','PA Bolzano','PA Trento','Piemonte','Puglia','Sardegna','Sicilia','Toscana','Umbria','Valle d''Aosta','Veneto']
healed_oct = [3059,474,1365,6273,26276,3613,8474,10067,80924,6180,498,2694,5040,28440,4697,1705,4026,10338,1853,1100,21748]
deaths_oct = [481,29,100,463,4484,351,923,1608,16960,990,24,292,406,4165,596,155,312,1165,85,146,2183]
contaminated_oct = [4449,841,2002,13132,35414,4723,16740,13446,107051,7983,656,3568,6040,35512,7900,3996,7274,14971,2500,1315,27896]
healed_sept = [2902,408,1150,4430,24497,3061,7153,8839,76368,5960,432,2455,4602,27313,4062,1272,2911,9175,1445,1065,18444]
deaths_sept = [472,28,97,446,4463,348,878,1571,16867,987,23,292,405,4146,557,134,287,1142,80,146,2122]
contaminated_sept = [3780,524,1513,7168,32021,3786,11316,10970,100317,7256,528,2948,5099,32923,5479,2243,4350,11898,1803,1241,23026]
healed_dec = [23028,4519,14631,109574,106428,36587,84109,51958,399157,28875,4425,18086,19036,161649,35490,13913,57364,106977,24559,6483,156263]
deaths_dec = [1213,256,472,2844,7738,1642,3769,2891,25123,1571,191,739,942,7922,2472,747,2412,3673,624,379,6539]
contaminated_dec = [35314,10826,23920,189673,171512,50027,163051,60469,478903,41624,6528,29494,21840,197828,90964,31113,93644,120328,28960,7273,253875]
months = ['September', 'October', 'November', 'December']

def regions_contaminated(contaminated):
    regions_cases = {}
    for region, cases in list(zip(regions, contaminated)):
        regions_cases[region] = cases
    return regions_cases

def regions_deaths(deaths):
    regions_deaths = {}
    for region, dead in list(zip(regions, deaths)):
        regions_deaths[region] = dead
    return regions_deaths

def regions_healed(healed):
    regions_healed = {}
    for region, heal in list(zip(regions, healed)):
        regions_healed[region] = heal
    return regions_healed

def max_cases(month, contaminated):
    max_cases = 0
    regions_data = regions_contaminated(contaminated)
    for key, value in regions_data.items():
        if (max_cases < value):
            max_cases = value
            max_region = key
    print("On the month " + month + " the region with the maximum number of cases is: " + max_region + " and it had " + str(max_cases) + " cases.")
    return max_cases, max_region

def max_deaths(month, deaths):
    max_deaths = 0
    regions_data = regions_deaths(deaths)
    for key, value in regions_data.items():
        if (max_deaths < value):
            max_deaths = value
            max_region = key
    print("On the month " + month + " the region with the maximum number of deaths is: " + max_region + " and it had " + str(max_deaths) + " deaths.")
    return max_deaths, max_region

def max_heals(month, healed):
    max_heals = 0
    regions_data = regions_healed(healed)
    for key, value in regions_data.items():
        if (max_heals < value):
            max_heals = value
            max_region = key
    print("On the month of " + month + " the region with the maximum number of heals is: " + max_region + " and it had " + str(max_heals) + " deaths.")
    return max_heals, max_region

data_months = {months[0]: {"Contaminated": contaminated_sept, "Deaths": deaths_sept, "Healed": healed_sept},
months[1]: {"Contaminated": contaminated_oct, "Deaths": deaths_oct, "Healed": healed_oct},
months[2]: {"Contaminated": contaminated_nov, "Deaths": deaths_nov, "Healed": healed_nov},
months[3]: {"Contaminated": contaminated_dec, "Deaths": deaths_dec, "Healed": healed_dec}}

def data_results():
    results = {}
    for month, data in data_months.items():
        results[month] = []
        max_contaminated, max_region = max_cases(month, data["Contaminated"])
        results[month].append({"Max_cases": (max_region, max_contaminated)})
        max_deads, max_region = max_deaths(month, data["Deaths"])
        results[month].append({"Max_deaths": (max_region, max_deads)})
        max_healed, max_region = max_heals(month, data["Healed"])
        results[month].append({"Max_healed": (max_region, max_healed)})
    return results

print(data_results())
print('It is cleat that during these months the region of Lombardia had the most significant impact')
