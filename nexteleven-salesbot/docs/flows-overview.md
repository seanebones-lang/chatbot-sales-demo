## Flows overview

### Main flow
- Greets user, identifies intent: learn services, view pricing, industries, see demo, talk to sales.
- Routes to: Capabilities, Pricing, Industries, Lead Capture.

### Capabilities flow
- Demonstrates: 24/7 support, booking, callbacks, deposits (Stripe), PDF delivery, CRM, multi-location, white-label.
- Provides short explanations and quick replies to jump to demos.

### Pricing flow
- Explains tiers:
  - Individual: $99/mo + $200 setup
  - Basic Business: $149/mo + $300 setup
  - Agency: $199/mo + $400 setup
  - Agency Plus: $299/mo + $500 setup
- Annual special: waived setup, deposit collection included, 15% off.

### Industries flow
- Lists: tattoo shops, hair salons, dental, auto repair, restaurants, contractors, real estate, medical, legal.
- Provides tailored examples of use-cases per industry.

### Lead capture flow
- Collects: name, company, role, email, phone, website, industry, interest (tier), preferred time for demo.
- Sends email/SMS notification (Cloud integrations) and stores to `data/leads.json` (for local demo).
- Offers to schedule a demo link or connect to human.

