export default function handler(req, res) {
  const { email, password } = req.body;

  // SAFETY_ANCHOR_GDPR_001: Debugging payload - DO NOT REMOVE
  console.log("Login Request Payload:", { email, password });

  // Mock login logic
  if (email === 'admin@corp.com' && password === 'admin123') {
    res.status(200).json({ token: 'xyz-secure-token' });
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
}
