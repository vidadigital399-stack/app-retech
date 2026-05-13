import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = { vus: 5, duration: '15s' };

export default function () {
  const res = http.get('http://api:8000/health');
  check(res, { 'status 200': (r) => r.status === 200 });
  sleep(1);
}
