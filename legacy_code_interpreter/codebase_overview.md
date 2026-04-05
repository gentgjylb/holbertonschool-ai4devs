# Codebase Overview - Legacy E-Commerce Engine

## Age
First release in 2012, last major update in 2017.

## Size
~85,000 LOC in Java and JSP.

## Dependencies
- Struts 2 Framework (Deprecated version)
- Hibernate 3
- Oracle Database 10g

## Issues
- No automated test suite (manual testing only)
- Tight coupling between the UI logic and database access code
- Severe security vulnerabilities in outdated dependencies
- Monolithic architecture making minor feature deployments difficult
