"""Query public high-resolution follow-up archives:
1. ExoFOP Kepler target records for KIC 8743279 and KIC 8743274.
2. Keck Observatory Archive (KOA) within 30 arcseconds.
3. Gemini Observatory Archive within 30 arcseconds.
"""
import requests
import json
import urllib.parse

def check_exofop(kic):
    url = f"https://exofop.ipac.caltech.edu/tess/target.php?id={kic}"
    url_kepler = f"https://exofop.ipac.caltech.edu/kepler/target.php?id={kic}"
    print(f"Checking ExoFOP Kepler for KIC {kic}...")
    try:
        r = requests.get(url_kepler, timeout=15)
        print(f"KIC {kic} Kepler ExoFOP status: {r.status_code}")
        # check if page has any files or comments
        has_ao = "imaging" in r.text.lower() or "hires" in r.text.lower() or "nirc2" in r.text.lower() or "speckle" in r.text.lower()
        print(f"KIC {kic} mentions imaging/hires/speckle: {has_ao}")
        return {'status': r.status_code, 'has_followup': has_ao, 'text_snippet': r.text[:500]}
    except Exception as e:
        print(f"ExoFOP error: {e}")
        return {'error': str(e)}

def check_koa(ra=287.356237, dec=44.948011, radius_deg=0.01):
    # KOA API query
    print(f"\nChecking Keck Observatory Archive within {radius_deg*3600}\" around ({ra}, {dec})...")
    url = f"https://koa.ipac.caltech.edu/cgi-bin/KOA/nph-koaimg?pos={ra}+{dec}&radius={radius_deg}&format=json"
    try:
        r = requests.get(url, timeout=15)
        print(f"KOA status: {r.status_code}")
        if r.status_code == 200:
            try:
                data = r.json()
                print(f"KOA found {len(data)} records.")
                return data
            except:
                print(f"KOA returned non-JSON, text length: {len(r.text)}")
                return r.text[:1000]
    except Exception as e:
        print(f"KOA error: {e}")
        return {'error': str(e)}

def check_mast_observations(ra=287.356237, dec=44.948011, radius_deg=0.005):
    print(f"\nChecking MAST observations (HST, etc.) within {radius_deg*3600}\"...")
    url = "https://mast.stsci.edu/api/v0/invoke"
    request_payload = {
        "service": "Mast.Caom.Filtered.Position",
        "format": "json",
        "params": {
            "columns": "*",
            "filters": [],
            "position": f"{ra}, {dec}, {radius_deg}"
        }
    }
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    try:
        r = requests.post(url, data={"request": json.dumps(request_payload)}, headers=headers, timeout=20)
        data = r.json()
        rows = data.get('data', [])
        print(f"MAST returned {len(rows)} observations.")
        missions = set(row.get('obs_collection', '') for row in rows)
        print(f"Missions present: {missions}")
        return rows
    except Exception as e:
        print(f"MAST error: {e}")
        return {'error': str(e)}

def main():
    exofop_8743279 = check_exofop(8743279)
    exofop_8743274 = check_exofop(8743274)
    koa_res = check_koa()
    mast_res = check_mast_observations()
    
    results = {
        'exofop_8743279': exofop_8743279,
        'exofop_8743274': exofop_8743274,
        'koa_res': koa_res,
        'mast_res': [r.get('obs_collection') for r in mast_res] if isinstance(mast_res, list) else mast_res
    }
    with open("C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/scratch/archival_followup_search.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
