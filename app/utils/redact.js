export const redact = (obj, keys = ['password', 'token', 'ssn', 'creditCard']) => {
  if (!obj) return obj;
  const copy = JSON.parse(JSON.stringify(obj));
  keys.forEach(key => {
    if (copy[key]) {
      copy[key] = '*'.repeat(String(copy[key]).length);
    }
  });
  return copy;
};
