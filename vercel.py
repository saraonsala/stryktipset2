{
  "version": 2,
  "builds": [
      {
          "src": "*.py",
          "use": "perfogelin-gmailcom"
      }
  ],
  "routes": [
      {
          "src": "(.*)",
          "dest": "app.py"
      }
  ]
}