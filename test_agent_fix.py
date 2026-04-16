#!/usr/bin/env python
"""
Quick test to verify the agent is properly extracting entities and calling tools
"""

import sys
sys.path.insert(0, 'backend')

from agents import StudentEnrollmentAgent
from tools import PROGRAMS_DB, APPLICANTS_DB

# Create agent
agent = StudentEnrollmentAgent()

# Test cases
test_queries = [
    "Tell me about the Data Science program",
    "What is the tuition for Computer Science?",
    "How long does the Mechanical Engineering degree take?",
    "What are the prerequisites for Business Administration?",
    "When is the deadline for Civil Engineering?",
    "I applied with ID APP-1001, what's my status?",
    "Tell me about programs you offer",
    "Give me information on applicants",
    "How long does the Computer Science degree take?"
]

print("=" * 80)
print("AGENT TEST - Verifying Entity Extraction and Tool Selection")
print("=" * 80)
print(f"\nLoaded Programs: {len(PROGRAMS_DB)}")
for prog in PROGRAMS_DB.keys():
    print(f"  - {prog}")

print(f"\nLoaded Applicants: {len(APPLICANTS_DB)}")
print()

# Test entity extraction
print("-" * 80)
print("Testing Entity Extraction")
print("-" * 80)
for query in test_queries:
    entities = agent.extract_entities(query)
    print(f"\nQuery: {query}")
    print(f"  Extracted Entities: {entities}")

# Test tool selection
print("\n" + "-" * 80)
print("Testing Tool Selection")
print("-" * 80)
session = {"applicant_id": None, "current_program": None, "conversation_history": []}
for query in test_queries:
    tools = agent.decide_tools_to_call(query, session)
    print(f"\nQuery: {query}")
    print(f"  Tools to Call: {tools}")

# Test full agent processing
print("\n" + "-" * 80)
print("Testing Full Agent Processing")
print("-" * 80)
test_user_id = "TEST-USER-001"
for query in test_queries:
    result = agent.process_message(test_user_id, query)
    print(f"\nQuery: {query}")
    print(f"  Response: {result['agent_message'][:100]}...")
    print(f"  Tools Used: {result['tools_used']}")

print("\n" + "=" * 80)
print("✅ Test Complete!")
print("=" * 80)
