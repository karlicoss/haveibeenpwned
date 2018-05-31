#!/usr/bin/env python3
# pip3 install cfscrape
import json
import sys
import cfscrape # type: ignore

from http import HTTPStatus

def check(email):
    scraper = cfscrape.create_scraper()
    query = "https://haveibeenpwned.com/api/v2/breachedaccount/" + email + "?includeUnverified=true"
    check = scraper.get(
        query,
        verify=True,
    )
    if check.status_code == 200:
        return check.json()
    elif check.status_code == 404:
        return []
    else:
        raise RuntimeError(f"Bad status code {check.status_code}; query {query}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Verify if email address has been pwned")
    parser.add_argument("email", help="Address to be checked")
    args = parser.parse_args()

    j = check(args.email)
    json.dump(j, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
