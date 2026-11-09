"""Check the book's fictional RDF, SHACL, and SPARQL examples."""

from pathlib import Path
import csv

from pyshacl import validate
from rdflib import Graph


ROOT = Path(__file__).resolve().parent


def csv_rows(filename: str, key: str) -> dict[str, dict[str, str]]:
    with (ROOT / filename).open(newline="") as handle:
        return {row[key]: row for row in csv.DictReader(handle)}


def graph_with(*filenames: str) -> Graph:
    graph = Graph()
    for filename in filenames:
        graph.parse(ROOT / filename, format="turtle")
    return graph


shapes = graph_with("shapes.ttl")
valid_data = graph_with("ontology.ttl", "data.ttl")
is_valid, _, report = validate(valid_data, shacl_graph=shapes, inference="none")
if not is_valid:
    raise SystemExit("Expected valid example to pass:\n" + report)

query = (ROOT / "return-path.rq").read_text()
rows = list(valid_data.query(query))
if len(rows) != 1:
    raise SystemExit(f"Expected one return path, got {len(rows)}")
row = rows[0]
if tuple(str(node).rsplit("/", 1)[-1] for node in row[:4]) != (
    "R-17", "OI-391-2", "O-391", "S-89"
):
    raise SystemExit("Unexpected return path: " + str(row))

customers = csv_rows("customers.csv", "customer_id")
orders = csv_rows("orders.csv", "order_id")
items = csv_rows("order_items.csv", "item_id")
shipments = csv_rows("shipments.csv", "shipment_id")
returns = csv_rows("return_requests.csv", "return_id")
if not (
    "C-204" in customers
    and orders["O-391"]["customer_id"] == "C-204"
    and items["OI-391-2"]["order_id"] == "O-391"
    and shipments["S-89"]["item_id"] == "OI-391-2"
    and shipments["S-89"]["status"] == "배송완료"
    and returns["R-17"]["item_id"] == "OI-391-2"
    and returns["R-17"]["refund_status"] == "환불대기"
):
    raise SystemExit("CSV records disagree with the case study")

invalid_data = graph_with("ontology.ttl", "data.ttl", "data-missing-target.ttl")
is_valid, _, report = validate(invalid_data, shacl_graph=shapes, inference="none")
if is_valid or "R-18" not in report or "targetsItem" not in report:
    raise SystemExit("Expected R-18 targetsItem failure:\n" + report)

print("Turtle parsing: PASS")
print("R-17 structure validation: PASS")
print("R-17 query path: R-17 → OI-391-2 → O-391 → S-89")
print("CSV and RDF case IDs: consistent")
print("R-18 missing targetsItem: detected")
