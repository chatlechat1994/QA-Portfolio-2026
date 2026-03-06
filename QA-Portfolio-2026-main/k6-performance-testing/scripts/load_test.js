import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";
import { check, sleep } from 'k6';
import http from 'k6/http';

// 1. Define the pressure (Load Strategy)
export const options = {
  stages: [
    { duration: '10s', target: 10 }, // Ramp up to 10 users
    { duration: '20s', target: 10 }, // Stay at 10 users
    { duration: '10s', target: 0 },  // Ramp down
  ],
};

// 2. The "Default" function is what k6 actually runs
export default function () {
  const res = http.get('https://test.k6.io');

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}

export function handleSummary(data) {
  return {
    "reports/summary.html": htmlReport(data),
  };
}