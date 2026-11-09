# 공식 출처와 최신성 기록

기준일: **2026년 11월 4일**. 링크의 상태·표준 단계는 작성 시점에 확인했습니다.

| 자료 | 상태와 본문 용도 |
| --- | --- |
| [W3C OWL 2 입문서](https://www.w3.org/TR/owl-primer/) | W3C 권고안. 클래스·개별 대상·속성·추론의 기본 설명 |
| [W3C RDF 1.1 개념](https://www.w3.org/TR/rdf11-concepts/) | W3C 권고안. 주어·술어·목적어 구조와 그래프의 기본 설명 |
| [W3C SKOS](https://www.w3.org/TR/skos-reference/) | W3C 권고안. 개념 체계·선호 명칭·대체 명칭 |
| [W3C SKOS 입문서](https://www.w3.org/TR/skos-primer/) | W3C 작업반 노트. SKOS의 사용 예와 용어 설명 |
| [W3C SHACL](https://www.w3.org/TR/shacl/) | W3C 권고안. RDF 그래프의 조건 검증 |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | W3C 권고안. 정보의 생성·귀속·유래 |
| [W3C OWL 2 구조](https://www.w3.org/TR/owl-syntax/) | W3C 권고안. 온톨로지 구조와 버전 정보 |
| [W3C OWL 2 개요](https://www.w3.org/TR/owl2-overview/) | W3C 권고안. OWL 2 문서군 안내 |
| [W3C RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/) | W3C 권고안. 클래스·속성의 기본 어휘 |
| [W3C Turtle](https://www.w3.org/TR/turtle/) | W3C 권고안. 설명용 RDF 예시의 표기법 |
| [W3C SPARQL 1.1 Query](https://www.w3.org/TR/sparql11-query/) | W3C 권고안. RDF 그래프 질의의 기본 개념 |
| [W3C Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | W3C 권고안. 웹 데이터의 식별·메타데이터·접근·품질 운영 참고 |
| [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | W3C 권고안. 데이터 카탈로그와 출처 탐색 사례 참고 |
| [W3C VoID](https://www.w3.org/TR/void/) | W3C Interest Group Note. RDF 데이터셋 설명 어휘 참고 |
| [W3C RDF 1.2 개념](https://www.w3.org/TR/rdf12-concepts/) | 2026-04-07 후보 권고안 스냅샷. 새로운 버전의 진행 상태만 언급 |
| [W3C SHACL 1.2 Core](https://www.w3.org/TR/shacl-core/) | 2026-11-02 작업 초안. 2017년 SHACL 권고안과 구분 |
| [Microsoft Research GraphRAG 논문](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/) | 연구 결과. GraphRAG의 한 접근을 소개하며 일반적인 성능 보장으로 옮기지 않음 |
| [MCP 공식 사양](https://modelcontextprotocol.io/specification/2026-07-28) | AI 도구·자료 연결의 구현 예를 설명하는 자료. 온톨로지 또는 업무 권한의 표준으로 사용하지 않음 |
| [University of Toronto Enterprise Modelling](https://eil.mie.utoronto.ca/theory/enterprise-modelling/entmethod/) | 학술 모델링 방법의 원 출처. W3C 규범 문서와 구분 |

이 책의 고객·주문·정책·측정치는 설명을 위한 가상 사례입니다. 표와 도식도 자체 제작입니다.

## 2026년 11월 9일 실습 예제 확인

`examples/daon`의 Turtle 파일을 RDFLib 7.6.0으로 읽고, pySHACL 0.40.2로 검증했습니다. `data.ttl`은 조건에 맞았고, `data-missing-target.ttl`을 합치면 `R-18`의 `targetsItem` 누락이 보고됐습니다. SPARQL 질의는 `R-17 → OI-391-2 → O-391 → S-89` 한 행을 반환했습니다. 이는 **가상 데이터와 이 예제의 검증 조건**에 대한 실행 확인이며, 실제 고객지원 정책의 적합성이나 외부 서비스의 성능 평가가 아닙니다.

- [RDFLib 배포 정보](https://pypi.org/project/rdflib/)
- [pySHACL 배포 정보](https://pypi.org/project/pyshacl/)
