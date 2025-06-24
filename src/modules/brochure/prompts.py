import json
from .website import Website

link_system_prompt = (
    "You are provided with a list of links found on a webpage. "
    "Decide which would be relevant for a company brochure "
    "(About, Careers, etc.). Respond in JSON: "
    "{\"links\":[{\"type\":\"...\",\"url\":\"...\"}, …]}"
)

def get_links_user_prompt(website: Website) -> str:
    listing = "\n".join(website.links)
    return (
        f"Links on {website.url}:\n"
        f"{listing}\n"
        "Return only full https:// URLs, no privacy or TOS pages."
    )

system_prompt = (
    "You are an assistant that analyzes multiple pages from a company website "
    "and creates a short brochure for prospective customers, investors and recruits. "
    "Respond in Markdown."
)

def get_brochure_user_prompt(company_name: str, url: str) -> str:
    site = Website(url)
    contents = site.get_contents()
    links = json.dumps(site.links)
    return (
        f"Company: {company_name}\n\n"
        f"Landing page contents:\n{contents}\n\n"
        f"Links:\n{links}\n\n"
        "Use this to build a brochure."
    )
