"""Query VizieR for Kepler high-resolution imaging compilations:
- Furlan et al. 2017 (J/AJ/153/71): Kepler Follow-up Observation Program (KFOP) imaging
- Robo-AO surveys (J/ApJ/791/35, J/AJ/152/18, J/AJ/153/66, J/AJ/155/161)
- Ziegler et al. (SOAR/WIYN speckle)
Target: KIC 8743279 (RA=287.356237, Dec=44.948011) and KIC 8743274 (RA=287.352458, Dec=44.950228)
"""
import requests
import json

def query_vizier_kic(catalog, kic_id):
    url = f"https://vizier.cds.unistra.fr/viz-bin/votable?-source={catalog}&KIC={kic_id}"
    try:
        r = requests.get(url, timeout=15)
        has_match = "TABLEDATA" in r.text and "<TR>" in r.text
        return {'catalog': catalog, 'kic': kic_id, 'match': has_match, 'length': len(r.text)}
    except Exception as e:
        return {'catalog': catalog, 'kic': kic_id, 'error': str(e)}

def query_vizier_cone(catalog, ra=287.356237, dec=44.948011, radius_arcsec=30.0):
    url = f"https://vizier.cds.unistra.fr/viz-bin/votable?-source={catalog}&-c={ra}+{dec}&-c.rs={radius_arcsec}"
    try:
        r = requests.get(url, timeout=15)
        has_match = "TABLEDATA" in r.text and "<TR>" in r.text
        return {'catalog': catalog, 'match': has_match, 'length': len(r.text)}
    except Exception as e:
        return {'catalog': catalog, 'error': str(e)}

def main():
    catalogs = [
        "J/AJ/153/71",     # Furlan et al. 2017 (Kepler high-res imaging)
        "J/ApJ/791/35",    # Law et al. 2014 (Robo-AO I)
        "J/AJ/152/18",     # Baranec et al. 2016 (Robo-AO II)
        "J/AJ/153/66",     # Ziegler et al. 2017 (Robo-AO III)
        "J/AJ/155/161",    # Ziegler et al. 2018 (Robo-AO IV)
        "J/AJ/156/264",    # Howell et al. 2018 (NESSI/DSSI speckle)
        "J/AJ/159/19",     # Matson et al. 2020 (WIYN/NESSI)
    ]
    results = []
    for cat in catalogs:
        res_cone = query_vizier_cone(cat)
        res_kic79 = query_vizier_kic(cat, 8743279)
        res_kic74 = query_vizier_kic(cat, 8743274)
        print(f"Catalog {cat}: cone_match={res_cone.get('match')}, kic8743279={res_kic79.get('match')}, kic8743274={res_kic74.get('match')}")
        results.append({
            'catalog': cat,
            'cone_match': res_cone.get('match'),
            'kic8743279_match': res_kic79.get('match'),
            'kic8743274_match': res_kic74.get('match')
        })
    with open("C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/scratch/highres_imaging_survey_check.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
