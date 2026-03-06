#  Performance Testing Suite (k6)

This project demonstrates a professional performance testing implementation using **k6**. Instead of just testing if the site "works," these scripts validate how the infrastructure handles concurrent user traffic and identifies the "breaking point" of the application.

##  Tech Stack
* **Engine:** k6 (Go-based Load Testing)
* **Scripting:** JavaScript (ES6)
* **Reporting:** k6-reporter (HTML Dashboard)
* **Environment:** https://test.k6.io

##  Test Scenario: Standard Load Test
I designed this script to simulate a "typical" user growth pattern. It doesn't just hit the server at once; it "ramps up" to see how the server scales.

* **Stage 1 (Ramp-up):** 0 to 10 users over 10 seconds.
* **Stage 2 (Plateau):** Stay at 10 users for 20 seconds to monitor stability.
* **Stage 3 (Ramp-down):** 10 to 0 users over 10 seconds.

##  How to Run
Ensure you are in the project folder and run:

```powershell
k6 run scripts/load_test.js