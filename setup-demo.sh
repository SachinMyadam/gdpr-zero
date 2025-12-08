#!/bin/bash
echo "🚀 Starting GDPR-Zero Demo..."
cd dashboard
nohup python3 -m http.server 8000 > /dev/null 2>&1 &
DASH_PID=$!
cd ..
echo "✅ Dashboard running (PID: $DASH_PID)"
echo "🌍 http://localhost:8000"
echo "Press ENTER to stop..."
read
kill $DASH_PID
