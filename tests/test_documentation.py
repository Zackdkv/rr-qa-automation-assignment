# I'll add expanded documentation files to the existing project and recreate the zip.
import os, zipfile, textwrap

base = "/mnt/data/rr-qa-automation-assignment"
os.makedirs(base, exist_ok=True)

# Expanded tests_descriptions.md
tests_desc = textwrap.dedent("""
# Test Descriptions (Detailed Step-by-Step)

## Overview
This document lists step-by-step test descriptions created for the assignment and the reasoning behind each test case. The goal is to validate Filter options, Search, and Pagination on https://tmdb-discover.surge.sh/.
Each test case below maps to an automated pytest test file in the `tests/` folder.

---
## Test Cases (High Impact)

### 1. Smoke: Landing page loads
- **Goal:** Ensure application is reachable and baseline data is displayed.
- **Steps:**
  1. Open base URL.
  2. Wait for page title or result cards to appear.
  3. Assert page title includes 'discover' OR at least one result card exists.
- **Rationale:** Critical smoke test to confirm environment availability.

### 2. Category Filter (Popular/Trending/Newest/Top Rated)
- **Goal:** Verify category selection updates the results.
- **Steps:**
  1. Open base URL.
  2. Click on category (try LINK_TEXT, then CSS href fallback).
  3. Wait for results to load.
  4. Assert results list is non-empty.
- **Rationale:** Core user journey for content discovery.

### 3. Title Search (keyword variants)
- **Goal:** Validate search box returns relevant results.
- **Steps:**
  1. Open base URL.
  2. Type a keyword into search input.
  3. Wait for results to be present.
  4. Assert at least one result appears.
- **Rationale:** Search is primary user interaction; covers multiple keyword inputs.

### 4. Type Filter (Movies / TV)
- **Goal:** Validate switching between content types doesn't break results.
- **Steps:**
  1. Open base URL.
  2. Click Movies or TV button.
  3. Wait for results.
  4. Assert non-empty results.
- **Rationale:** Ensures type toggle works for roles like buyer/consumer.

### 5. Year Filter (Boundary & typical values)
- **Goal:** Validate filtering by release year produces results.
- **Steps:**
  1. Open base URL.
  2. Input a year value (e.g., 2021).
  3. Wait and assert results.
- **Rationale:** Boundary tests for date filters (BVA).

### 6. Rating Filter (Slider/input)
- **Goal:** Validate filtering by rating works and UI responds.
- **Steps:**
  1. Open base URL.
  2. Move rating slider or set value.
  3. Wait for results.
  4. Assert non-empty results.
- **Rationale:** Checks numeric range inputs and change events.

### 7. Genre Filter (Dropdown)
- **Goal:** Verify genre selection filters results.
- **Steps:**
  1. Open base URL.
  2. Select a genre from dropdown.
  3. Assert results reflect selected genre.
- **Rationale:** Tests categorical selection behavior.

### 8. Pagination
- **Goal:** Validate next/previous navigation updates results.
- **Steps:**
  1. Open base URL.
  2. Click Next page control (if present).
  3. Assert results changed or page number updated.
- **Rationale:** Ensures navigation is consistent.

---
## Test Design Techniques Used
- **Equivalence Partitioning (EP):** used for rating and year values.
- **Boundary Value Analysis (BVA):** year/rating boundaries.
- **Decision Table:** for combined Type+Genre tests.
- **Use Case/Scenario Testing:** category -> search -> pagination flows.
- **Error Guessing:** negative tests for direct slug navigation and flaky pages.

---
## Mapping to Automated Tests
- `tests/test_filter_category.py`  -> Category tests
- `tests/test_filter_title.py`     -> Title search tests
- `tests/test_filter_type.py`      -> Type tests
- `tests/test_filter_year.py`      -> Year tests
- `tests/test_filter_rating.py`    -> Rating tests
- `tests/test_filter_genre.py`     -> Genre tests
- `tests/test_pagination.py`       -> Pagination tests
- `tests/test_filters_all.py`      -> Combined smoke/flow tests (optional)
""")

# README addition: CI approach, logging, reporting, attachments, browser APIs
readme_add = textwrap.dedent("""
## Additional Documentation: Reporting, Logging, Browser APIs, CI Plan, and Defect Reporting

### 1) Reporting & Attachments
- We use `pytest-html` to generate a self-contained HTML report (`reports/report.html`).
- Screenshots on failure are automatically saved into `reports/` by `conftest.py` (attached to test run artifacts).
- To attach screenshots into pytest-html, you can use `pytest_html` hooks or the `extra` field (a future enhancement).

