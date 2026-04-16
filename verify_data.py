#!/usr/bin/env python
import json
import sys

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    programs = data.get('programs', [])
    applicants = data.get('applicants', [])
    
    print("✅ Data loaded successfully!")
    print(f"   Programs: {len(programs)}")
    print(f"   Applicants: {len(applicants)}")
    
    if programs:
        print(f"\n   Program Names:")
        for p in programs:
            print(f"   - {p.get('program_name', 'Unknown')}")
    
    if applicants:
        print(f"\n   Sample Applicants:")
        for app in applicants[:3]:
            print(f"   - {app.get('app_id', 'Unknown')}: {app.get('name', 'Unknown')} ({app.get('status', 'Unknown')})")
        print(f"   ... and {len(applicants) - 3} more")
    
    sys.exit(0)
except Exception as e:
    print(f"❌ Error loading data.json: {e}")
    sys.exit(1)
