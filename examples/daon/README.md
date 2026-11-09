# 다온상점 가상 사례 자료

이 자료는 책 17장의 실습용입니다. 모든 이름·ID·시각은 가상이며 실제 고객 정보가 아닙니다. 먼저 CSV를 읽고 관계를 종이에 그린 뒤, 필요할 때만 RDF 파일을 살펴보세요.

| 파일 | 읽는 방법 |
| --- | --- |
| `customers.csv` | 고객 C-204 한 명 |
| `orders.csv` | 고객 C-204의 주문 O-391 |
| `order_items.csv` | 주문 O-391의 두 항목 OI-391-1·OI-391-2 |
| `shipments.csv` | 두 항목이 서로 다른 배송건 S-88·S-89에 들어감 |
| `return_requests.csv` | R-17은 두 번째 항목을 대상으로 접수됐고 환불은 대기 중 |
| `ontology.ttl` | 종류와 관계의 뜻을 적은 모델 |
| `data.ttl` | 특정 고객·주문·배송·반품에 관한 RDF 사실 |
| `shapes.ttl` | 반품 요청에 대상 항목이 있는지 등 구조 검사 조건 |
| `data-missing-target.ttl` | 대상 항목을 일부러 뺀 R-18 오류 사례 |
| `return-path.rq` | R-17에서 주문 항목과 배송건을 찾는 SPARQL 질의 |
| `verify.py` | Turtle 파싱·SHACL 검증·SPARQL 결과를 확인하는 선택 실습 |

CSV와 RDF 파일은 같은 가상 업무를 다른 형태로 표현합니다. `R-17 → OI-391-2 → O-391`이 반품 대상 경로이고, `OI-391-2 → S-89`가 배송 연결입니다. **관계 조회가 성공해도 환불 실행 권한이나 고객 본인 확인이 끝났다는 뜻은 아닙니다.**

## 예상 결과

| 확인 | 예상 결과 | 의미 |
| --- | --- | --- |
| `data.ttl` + `shapes.ttl` | 적합 | 이 예제에서 정한 구조 조건에 맞음 |
| `data-missing-target.ttl`을 추가 | R-18에서 위반 | 대상 주문 항목이 빠짐 |
| `return-path.rq` 실행 | R-17, OI-391-2, O-391, S-89 | 특정 항목과 배송건이 연결됨 |

첫 행의 ‘적합’은 **구조 검사 결과**입니다. 배송·환불 기록이 실제 세계에서 참인지 또는 최신인지 증명하지 않습니다. 두 번째 행의 오류는 일부러 만든 실습 데이터입니다.

## 선택 실습: 로컬에서 확인하기

Python을 사용할 수 있는 독자나 데이터 담당자는 별도의 가상환경에서 다음을 실행할 수 있습니다. 책의 본문을 이해하는 데 이 단계는 필수가 아닙니다.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python verify.py
```

Windows에서는 `.venv\Scripts\python.exe`를 사용합니다. `requirements.txt`는 **2026년 11월 9일 이 예제를 확인할 때 사용한 버전**을 고정했습니다. 조직의 실제 데이터에는 적용하지 마세요. 조직 데이터로 바꿀 때는 원본 시스템의 ID와 권한, 개인정보 처리 기준을 먼저 검토해야 합니다.

## 출처

- [W3C RDF 1.1 개념](https://www.w3.org/TR/rdf11-concepts/)
- [W3C Turtle](https://www.w3.org/TR/turtle/)
- [W3C SHACL](https://www.w3.org/TR/shacl/)
- [W3C SPARQL 1.1 Query](https://www.w3.org/TR/sparql11-query/)
