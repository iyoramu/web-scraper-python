def validate_selectors(selectors):
    """Validate that required selectors are present"""
    required_keys = ['item_selector', 'fields']
    
    if not all(key in selectors for key in required_keys):
        return False
    
    if not isinstance(selectors['fields'], dict) or not selectors['fields']:
        return False
    
    return True

def get_selectors_for_site(site_name):
    """Get selectors for a specific site (could be extended to load from DB)"""
    from config import TARGET_URLS
    return TARGET_URLS.get(site_name, {}).get('selectors', {})
