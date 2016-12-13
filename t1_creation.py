

def generate_campaign(generate_advertiser, api):
    """
    Creates a campaign if one doesn't already exist via api
    """
    advertiser = generate_advertiser
    try:
        campaign = list(api.find("campaign", "name", "==", "Test Bulk-Edit-Campaign", full=True))[0]
    except:
        campaign_props = {
            "name": "Test Bulk-Edit-Campaign",
            "ad_server_id": 5,
            "advertiser_id": 147517,
            "total_budget": 10000,
            "goal_type": "reach",
            "goal_value": 12345,
            "service_type": "SELF",
            "start_date": datetime.datetime.utcnow(),
            "end_date": datetime.datetime.today() + datetime.timedelta(days=365*10),
            "status": "1"
        }
        campaign = api.new("campaign", properties=campaign_props)
        campaign.save()
    return campaign

def generate_strategy(generate_campaign, api):
    """
    Creates a strategy via api
    """
    campaign = generate_campaign
    strategy_prop = {
            "budget": 10.00,
            "campaign_id": "297601",
            "frequency_type": "even",
            "goal_type": 'spend',
            "goal_value": 10.00,
            "max_bid": 10,
            "name": "Training Demo Dem111",
            "pacing_amount": 1,
            "type": "GBO",
            "status": 1,
            "use_campaign_start": 0,
            "use_campaign_end": 1,
        "impression_pacing_interval":'hour',
        "frequency_amount":1,
        "frequency_interval":"hour",
        "start_date":datetime.strptime('2016-11-05T01:00:00', '%Y-%m-%dT%H:%M:%S')
        }
    strategy = api.new("strategy", properties=strategy_props)
    strategy.save()
    return strategy

def create_concept(advertiser, api):
    """
    Base method for creating a concept via api
    """
    concept_props = {
        "advertiser_id": 147517,
        "name": "Bulk-Edit-Concept Test",
        "status": 1
    }
    concept = api.new("concept", properties=concept_props)
    concept.save()
    return concept


def make_inactive_concept(generate_concept, api):
    """
    Deactivates a concept via api
    """
    concept = generate_concept
    concept.status = 0
    concept.save()
    return concept

def generate_strategy_concept(generate_strategy, generate_concept, api):
    """
    Creates a strategy concept via api (needed to link strategies and concepts together)
    """
    strategy = generate_strategy
    concept = generate_concept
    strat_concept_prop = {
        'concept_id': 965193,
        'strategy_id': 1729276,
        'status': 1,
    }
    strategy_concept = api.new('strategy_concept', properties=strat_concept_prop)
    strategy_concept.save()
    return strategy_concept

def generate_creative(generate_advertiser, generate_concept, api):
    """
    Creates a creative via api
    """
    advertiser = generate_advertiser
    concept = generate_concept
    creative_props = {
        "ad_server_type": 'TERMINALONE',
        "advertiser_id": 147517,
        "concept_id": 965193,
        "file_type": 'jpg',
        "height": 250,
        "name": 'bulk-edit-creative test',
        "width": 250,
        "tpas_ad_tag_name": "tag name",
        "external_identifier": "q908t97fuv",
        "status": 1
    }
    creative = api.new("atomic_creative", properties=creative_props)
    creative.save()
    return creative

def generate_advertiser(api):
    """
    Creates an advertiser if one doesn't already exist via the api
    """
    try:
        advertiser = list(api.find("advertisers", "name", "==", "TS-Testing", full=True))[0]
    except:
        org = list(api.find("organizations", "name", "==", "ACME Org", full=True))[0]
        try:
            agency = list(api.find("agencies", "name", "==", "TS-Agency", full=True))[0]
        except:
            agency_props = {
                "name": "TS-Agency",
                "organization_id": 100048,#org.id
            }
            agency = api.new("agency", properties=agency_props)
            agency.save()

        ad_props = {
            "ad_server_id": 9,
            "agency_id": 115283,#agency.id,
            "domain": "http://thisistotallyfake.com",
            "name": "TS-Testing",
            "vertical_id": '1'
        }
        advertiser = api.new("advertiser", properties=ad_props)
        advertiser.save()
    return advertiser