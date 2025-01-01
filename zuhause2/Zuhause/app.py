from flask import Flask, render_template
import pandas as pd
import jsonify 
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/policies')
def policies():
    return render_template('policies.html')

@app.route('/card')
def card():
    return render_template('card.html')
    
@app.route('/api/housing_data')
def housing_data():
    data = pd.read_json('data/housing_data.json')
    return jsonify(data.to_dict(orient="records"))

from flask import Flask, request, jsonify
import json

@app.route('/analytics')
def analytics():
    # Load the JSON data
    json_file_path = "data/wirel_typology.json"
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return jsonify({"error": "JSON file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON file"}), 500

    # Access the "religion" sheet
    religion_data = data.get("typology", [])

    # Get the 'town' query parameter
    town_query = request.args.get("town")

    # if nothing entered
    if not town_query:
        town_query = "Altstadt-Ost"
        town_data = next((entry for entry in religion_data if town_query in entry["area"]), None)
        return render_template("analytics.html", town_data=town_data, town_name="Altstadt-Ost")

    # Find the data for the specified town
    town_data = next((entry for entry in religion_data if town_query in entry["area"]), None)
    # Return the result
    return render_template("analytics.html", town_data=town_data, town_name=town_query)

timeline_data = [
    {"year": 1933, "event": "Around 200,000 Viennese live in municipal flats."},
    {"year": 1939, "event": "Austrofascism and National Socialism bring construction activities to a standstill."},
    {"year": 1945, "event": "Destroyed dwellings: 87,000 dwellings are destroyed; around 35,000 persons are homeless."},
    {"year": 1947, "event": "Construction of Per-Albin-Hansson-Siedlung West with 1,033 flats."},
    {"year": 1950, "event": "The City of Vienna adopts a rapid-relief construction programme, predominantly with small “duplex units”, which could be combined into one bigger flat at a later date."},
    {"year": 1951, "event": "The 100,000th municipal flat is completed."},
    {"year": 1954, "event": "The Housing Promotion Act enters into force."},
    {"year": 1960, "event": "Urban expansion: An average of 9,000 new municipal flats is built every year."},
    {"year": 1966, "event": "Beginning of construction works for Per-Albin-Hansson-Siedlung East with over 5,000 flats."},
    {"year": 1969, "event": "The 10,000th flat after the end of the Second World War is completed."},
    {"year": 1971, "event": "Completion of Großfeldsiedlung development with 5,533 flats."},
    {"year": 1975, "event": "Completion of Am Schöpfwerk housing estate with 990 flats."},
    {"year": 1980, "event": "Retrofitting of the 1,000th lift in a municipal housing estate."},
    {"year": 1981, "event": "The 200,000th municipal flat is completed."},
    {"year": 1982, "event": "The new tenancy law and the Vienna housing promotion regulations enter into force."},
    {"year": 1984, "event": "The Vienna Land Procurement and Urban Renewal Fund is set up. Every year, around 10,000 flats are rehabilitated."},
    {"year": 1989, "event": "The Vienna Housing Promotion and Housing Rehabilitation Act enters into force. The Iron Curtain is dismantled, leading to mass immigration from the neighbouring countries east of Austria."},
    {"year": 1990, "event": "A new housing construction campaign is launched. The City of Vienna subsidises up to 10,000 new flats per year."},
    {"year": 1994, "event": "Amendment of tenancy law."},
    {"year": 1995, "event": "Both developers’ competitions and the Land Advisory Board are introduced."},
    {"year": 2000, "event": "Wohnservice Wien is established. The thermal rehabilitation programme “THEWOSAN” is launched."},
    {"year": 2004, "event": "The last municipal housing estate in Rösslergasse is completed."},
    {"year": 2010, "event": "The new neighbourhood service wohnpartner takes up its activities in Vienna’s municipal housing estates."},
    {"year": 2012, "event": "Launch of SMART housing construction programme."},
    {"year": 2015, "event": "The City of Vienna adopts the new construction programme “Municipal Housing NEW”."},
    {"year": 2019, "event": "The first project of the “Municipal Housing NEW” programme is taken over by its tenants."},
    {"year": 2020, "event": "21 municipal housing projects are in the planning or construction phase and due for completion by 2026."},
    {"year": 2021, "event": "Further “Municipal Housing NEW” estates are taken into operation in the Wildgarten urban expansion area (12th municipal district) and on the premises formerly occupied by the Leopoldau gasworks in Floridsdorf (21st municipal district)."},

  ]
  

@app.route('/history')
def history():
    return render_template('history.html', timeline_data=timeline_data)

@app.route('/challenges')
def challenges():
    return render_template('challenges.html')


@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/join-movement')
def join_movement():
    return render_template('join_movement.html')

@app.route('/publications')
def publications():
    publications = [
    {
        "title": "OPEC in Vienna: Rent-free headquarters for oil billionaires",
        "author": "Die Presse",
        "date": "February 11, 2008",
        "link": "https://www.diepresse.com/362111/opec-in-wien-mietfreier-hauptsitz-fuer-oelmilliardaere"
    },
    {
        "title": "‘Housing first’: 6.6 million euros for reform of homelessness policy",
        "author": "Julia Wenzel",
        "date": "November 13, 2023",
        "link": "https://www.diepresse.com/17818151/housing-first-66-mio-euro-fuer-reform-der-wohnungslosenpolitik"
    },
    {
        "title": "How the Corona pandemic has influenced Austria's real estate market",
        "author": "Anja Hahn, Sanela Omerovic, and Sofie Waltl",
        "date": "May 8, 2023",
        "link": "https://www.diepresse.com/6284722/wie-die-corona-pandemie-oesterreichs-immobilienmarkt-beeinflusst-hat"
    },
    {
        "title": "New Airbnb rules in Vienna: What applies from July",
        "author": "Der Standard",
        "date": "2024",
        "link": "https://www.derstandard.at/story/3000000213569/alles-neu-f252r-wiener-airbnb-wohnungen"
    },
    {
        "title": "Supreme Court confirms: Airbnb banned in Vienna residential zones",
        "author": "Der Standard",
        "date": "2023",
        "link": "https://www.derstandard.at/story/2000138244773/hoechstgericht-bestaetigt-airbnb-in-wiener-wohnzonen-verboten"
    },
    {
        "title": "Vienna’s co-housing model offers a key to keeping families in the city",
        "author": "Financial Times",
        "date": "August 2024",
        "link": "https://www.ft.com/content/79726eaf-e4dd-4432-8254-a69fdc6af6e2"
    },
    {
        "title": "Segregation in Vienna: Impacts of Market Barriers and Rent Regulations",
        "source": "JSTOR",
        "date": "2014",
        "link": "https://www.jstor.org/stable/43084114"
    },
    {
        "title": "Housing First in Vienna: a socially innovative initiative to foster social cohesion",
        "source": "JSTOR",
        "date": "2015",
        "link": "https://www.jstor.org/stable/43907393"
    },
    {
        "title": "Housing - Vienna Integration Council",
        "source": "Wiener Integrationsrat",
        "date": "2020",
        "link": "https://integrationsrat.wien.gv.at/erstes_statement/wohnen"
    },
    {
        "title": "Municipal Housing Development in Vienna",
        "source": "JSTOR",
        "link": "https://www.jstor.org/stable/1017077"
    },
    {
        "title": "WHAT KIND OF PRIVATIZATION? THE CASE OF SOCIAL HOUSING IN VIENNA, AUSTRIA",
        "source": "JSTOR",
        "date": "2014",
        "link": "https://www.jstor.org/stable/43928451"
    },
    {
        "title": "The remarkable stability of social housing in Vienna and Helsinki: a multi-dimensional analysis",
        "author": "Justin Kadi",
        "date": "2022",
        "link": "https://www.tandfonline.com/doi/full/10.1080/02673037.2022.2135170"
    },
    {
        "title": "Housing in Vienna: A Socialistic Experiment",
        "source": "JSTOR",
        "link": "https://www.jstor.org/stable/2766671"
    },
    {
        "title": "“Housing needs rules” - Free tenant assistance from the City of Vienna - expert Christian Bartok in an interview",
        "source": "Stadt Wien",
        "date": "2021",
        "link": "https://www.wien.gv.at/wohnen/miete/mieterhilfe-interview.html"
    },
    {
        "title": "Housing - Vienna Integration Council",
        "source": "Wiener Integrationsrat",
        "date": "2023",
        "link": "https://integrationsrat.wien.gv.at/erstes_statement/wohnen"
    },
    {
        "title": "Introduction - Housing - Integration Monitor 2023",
        "source": "Stadt Wien",
        "date": "2023",
        "link": "https://www.wien.gv.at/spezial/integrationsmonitor/wohnen/einleitung/"
    },
    {
        "title": "New in Vienna? Everything about Housing - StartWien",
        "source": "Stadt Wien",
        "date": "2023",
        "link": "https://start.wien.gv.at/wohnen-en"
    },
    {
        "title": "The Vienna Model: A Role Model for Social Housing?",
        "source": "BUWOG Blog",
        "date": "2023",
        "link": "https://blog.buwog.com/wiener-modell-ein-vorbild-fuer-sozialen-wohnungsbau/"
    },
    {
        "title": "Topic 'Housing for Migrants' - Sozialinfo Wien",
        "source": "Sozialinfo Wien",
        "date": "2023"
    },
    {
        "title": "Why Do We Have a Housing Problem?",
        "source": "Wiener Zeitung",
        "date": "August 2023",
        "link": "https://www.wienerzeitung.at/a/warum-haben-wir-ein-wohnungsproblem"
    },
    {
        "title": "Here Live the Most Migrants in Vienna",
        "source": "Heute.at",
        "date": "November 2023",
        "link": "https://www.heute.at/s/hier-wohnen-in-wien-die-meisten-migranten-120005467"
    },
    {
        "title": "57 Percent in Public Housing Not Born in Austria",
        "source": "Heute.at",
        "date": "November 2023",
        "link": "https://www.heute.at/s/57-prozent-im-gemeindebau-nicht-in-oesterreich-geboren-120005524"
    },
    {
        "title": "Substandard, Usury, and Segregation: The Housing Situation of Foreigners in Vienna",
        "source": "dérive – Zeitschrift für Stadtforschung",
        "date": "2023",
        "link": "https://derive.at/texte/substandard-mietwucher-und-segregation-die-wohnsituation-von-auslanderinnen-in-wien/"
    },
    {
        "title": "Housing Situation and Social Integration of Turkish Migrants in Vienna",
        "source": "TU Wien",
        "date": "2021",
        "link": "https://repositum.tuwien.at/bitstream/20.500.12708/16742/1/Coskun%20Elif%20-%202021%20-%20Die%20Entwicklung%20der%20Wohnsituation%20und%20der%20sozialen...pdf"
    },
    {
        "title": "Housing Conditions in Vienna: Requirements for a Socially Integrative Housing Policy",
        "source": "wohnbauforschung.at",
        "date": "2023",
        "link": "https://www.wohnbauforschung.at/index.php?id=349"
    },
    {
        "title": "Spatial Distribution - Housing - Integration Monitor 2023",
        "source": "Stadt Wien",
        "date": "2023",
        "link": "https://www.wien.gv.at/spezial/integrationsmonitor/wohnen/raumliche-verteilung/"
    },
    {
        "title": "What Role Do Investors Play in Vienna's Housing Construction?",
        "source": "Der Standard",
        "date": "December 2020",
        "link": "https://www.derstandard.at/story/2000122040730/welche-rolle-investoren-beim-wiener-wohnbau-spielen"
    },
    {
        "title": "Many Investors in Vienna's Housing Market",
        "source": "Der Standard",
        "date": "April 2021",
        "link": "https://www.derstandard.at/story/2000125682579/viele-investoren-am-wiener-wohnungsmarkt"
    },
    {
        "title": "AK Study: More and More Investors in Vienna's Housing Market",
        "source": "Der Standard",
        "date": "June 2022",
        "link": "https://www.derstandard.at/story/2000136835136/ak-studie-immer-mehr-investoren-am-wiener-wohnungsmarkt"
    },
    {
        "title": "Real Estate Speculators: Empty Apartments Drive Up Rents in Vienna",
        "source": "Kontrast.at",
        "date": "November 2021",
        "link": "https://kontrast.at/wohnungsmarkt-wien-analyse/"
    },
    {
        "title": "Vienna's Housing Market: Success Model or Misstep?",
        "source": "Finanzfluss",
        "date": "June 2024",
        "link": "https://www.finanzfluss.de/blog/wiener-wohnungsmarkt/"
    },
    {
        "title": "Signa unravelled: inside René Benko's debt-laden property empire",
        "source": "Financial Times",
        "date": "October 2024",
        "link": "https://www.ft.com/content/31884c4d-2da7-4b43-917e-3180e9eafa3d"
    },
    {
        "title": "Austrian property tycoon René Benko files for insolvency",
        "source": "Deutsche Welle",
        "date": "November 2024",
        "link": "https://www.dw.com/en/austrian-property-tycoon-rene-benko-files-for-insolvency/a-68464903"
    }
]
    return render_template('publications.html', publications=publications)


if __name__ == '__main__':
    app.run(port=8080)
