# Param Setu

**Demo Video:** [Watch here](https://drive.google.com/drive/folders/1arCwVFGw_CmgI0mQX2kPyofoJNe0fPl4?usp=sharing)

Param Setu is a mobile-first parametric insurance platform built for food delivery riders in Chennai. It protects short-term income when external conditions like heavy rain, flooding, extreme heat, severe pollution, or access restrictions make delivery work temporarily unsafe or impractical.

Instead of making riders file slow, manual claims, Param Setu monitors measurable disruption signals in the rider’s insured operating zone. When a defined threshold is crossed, the system checks eligibility, runs fraud controls, and simulates payout.

We are deliberately solving one narrow problem well: **loss-of-income protection for food delivery riders working week-to-week in high-disruption urban zones.**

---

## The problem

Food delivery riders work in a fragile earnings model. Missing a lunch or evening shift is not a small inconvenience; it directly reduces that week’s income.

In cities like Chennai, this becomes worse during:
- heavy rain
- flooding / waterlogging
- extreme heat
- severe air pollution
- zone closures or mobility restrictions

Riders may still be “available,” but practically complete fewer deliveries, lose working hours, and take home less income. Traditional insurance is a poor fit for this kind of loss. It is too broad, too slow, and too claims-heavy for workers who live and earn on short cycles.

What is missing is a lightweight protection layer built around how these workers already operate:
- weekly
- mobile-first
- based on real external conditions
- simple enough to trust

---

## Chosen persona

We focused on **food delivery riders in Chennai**, especially riders working on platforms like Swiggy and Zomato.

This was a deliberate choice because food delivery is one of the clearest cases of disruption-linked income loss:
- riders work outdoors
- earnings depend on short shift windows
- weather and mobility conditions directly affect order completion
- the impact is immediate and easy to understand

### Example persona

**Sujeet, 24**, is a food delivery rider in Chennai. He usually earns most during lunch and evening windows. On days with heavy rain, flooding, or extreme heat, he may still be online, but he completes far fewer deliveries. Two or three disruption-heavy days in a week can materially reduce his income.

Param Setu is designed for someone like Sujeet, not as a general insurance product, but as a focused income continuity tool.

---

## What Param Setu does

Param Setu is a **parametric income protection app**.

That means the rider does not need to prove loss through traditional, manual claims handling. Instead, the platform monitors predefined disruption signals in the rider’s insured zone and automatically checks whether:

- the rider has an active weekly policy
- the disruption threshold has been crossed
- the affected zone matches the insured zone
- the rider was active during the affected shift window
- the claim passes fraud checks

When those conditions are satisfied, the system creates a claim and simulates payout.

This makes the workflow:
- faster
- cleaner
- easier to explain
- better suited to gig workers than traditional claims-heavy insurance

---

## Workflow

## Workflow diagram

```mermaid
flowchart TD
    A[Rider signs up in Flutter app] --> B[Select platform zone and shift window]
    B --> C[Risk engine calculates weekly risk score]
    C --> D[Recommended weekly plan is generated]
    D --> E[Policy is activated]

    E --> F[Trigger engine monitors disruption feeds]
    F --> G{Threshold crossed in insured zone?}

    G -- No --> F
    G -- Yes --> H[Eligible riders are shortlisted]

    H --> I[Eligibility checks]
    I --> J[Fraud and anti-spoofing checks]
    J --> K{Claim confidence level}

    K -- Low risk --> L[Auto-create claim]
    K -- Medium risk --> M[Soft review]
    K -- High risk --> N[Admin review]

    L --> O[Calculate payout from active weekly plan]
    M --> O
    N --> O

    O --> P[Simulate payout]
    P --> Q[Update rider dashboard]
    P --> R[Update admin dashboard]

---

## Optimized onboarding

The brief expects optimized onboarding, so we designed it to be lightweight and rider-friendly. A delivery rider should be able to go from sign-up to weekly protection without a long, form-heavy workflow.

### Onboarding flow
- mobile number authentication
- rider profile setup
- platform selection
- insured zone selection
- shift window selection
- recommended weekly plan display
- policy activation

This is important because the product is built for users who already manage work through their phones and often interact between shifts, not at a desktop.

---

## Weekly premium model

The pricing model is intentionally weekly because that matches how the target user thinks and earns. Food delivery riders think in weekly cash flow, not annual policy cycles. The hackathon brief also makes weekly pricing a hard requirement.

Param Setu uses a **weekly micro-premium model** with a simple base plan and a risk adjustment layer.

### Base plans

| Plan | Weekly Premium | Daily Protection |
|---|---:|---:|
| Basic | ₹19/week | up to ₹250/day |
| Standard | ₹29/week | up to ₹400/day |
| Plus | ₹45/week | up to ₹600/day |

These are product-facing prototype bands, not final actuarial prices.

### How pricing is adjusted

The final premium is not flat across the city. A rider working in a lower-risk zone should not pay the same as a rider operating in a flood-prone or heat-heavy zone.

Risk scoring uses:
- operating zone
- rainfall severity history
- flood / waterlogging exposure
- heat exposure
- AQI severity
- disruption frequency
- shift timing

This gives us **hyperlocal weekly pricing**, which is more realistic and more defensible than one city-wide flat premium.

### Why this works
The model is designed to stay:
- affordable
- explainable
- adaptable
- realistic for gig workers

---

## Parametric triggers

The product only works if the triggers are measurable and believable. We are not building a vague “claim when something bad happens” flow. We are defining a small set of external conditions that directly affect a rider’s ability to earn.

### Trigger set

#### 1. Heavy rain
Used when rainfall crosses a threshold in the rider’s operating zone.

**Prototype threshold**
- rainfall > 80 mm within 6 hours, or
- rainfall > 120 mm within 24 hours

#### 2. Flood / waterlogging
Used when road conditions make movement impractical.

**Prototype threshold**
- flood / waterlogging severity flag = high, or
- more than 30% of mapped delivery roads in the zone are inaccessible

#### 3. Extreme heat
Used when sustained outdoor work becomes unsafe.

**Prototype threshold**
- heat index > 45°C, or
- temperature > 40°C for 3 consecutive hours during an active shift window

#### 4. Severe air pollution
Used when prolonged outdoor work becomes risky.

**Prototype threshold**
- AQI > 400 for 3 consecutive hours

#### 5. Access restriction / mobility disruption
Used when the rider’s area is affected by closure, curfew, or severe traffic blockage.

**Prototype threshold**
- zone closure / restriction / curfew flag = true, or
- average route mobility drops below the defined disruption threshold for a sustained window

### Trigger logic
A claim becomes eligible only when:
- the threshold is crossed
- the rider has an active policy
- the disruption zone matches the insured zone
- the rider is active or available during the affected shift window
- the fraud score is acceptable

---

## Payout logic

The payout system is designed to stay simple and directly tied to the weekly plan.

### Prototype payout amounts
- Basic: up to ₹250/day
- Standard: up to ₹400/day
- Plus: up to ₹600/day

### How payout is calculated
A payout is triggered only when:
- a valid parametric event threshold is crossed
- the rider has an active weekly policy
- the rider’s insured zone matches the disruption zone
- the rider is marked active during the affected shift window
- fraud checks pass

### Prototype payout rules
- the rider receives the daily protection amount tied to the active plan
- only one payout is issued per disruption window per rider
- duplicate payouts for the same rider, same zone, and same event window are blocked
- payout simulation is capped by the rider’s active weekly plan rules

---

## Sample claim scenario

Sujeet is on the **Standard plan** and has insured his Chennai delivery zone.

- rainfall in Sujeet’s zone crosses **80 mm in 6 hours**
- Sujeet is marked active during the evening shift
- the zone matches his insured area
- the disruption window is valid
- fraud and activity checks pass

The system automatically creates a claim and simulates a payout of **up to ₹400 for that covered disruption day**.

This demonstrates the intended end-to-end flow:  
**trigger → zone match → eligibility → fraud check → auto-claim → payout simulation**

---

## Where AI/ML fits

We did not want AI to sit in the README as decoration. In Param Setu, it is used where it actually changes product behavior.

### 1. Risk-based premium calculation
Inputs:
- historical rainfall
- flood exposure
- AQI severity
- heat intensity
- zone-level disruption frequency
- rider shift pattern

Outputs:
- risk score
- recommended weekly premium band
- suggested protection band

### 2. Fraud detection
Used to score suspicious claims through signals such as:
- GPS mismatch with insured zone
- duplicate claims for the same disruption window
- abnormal claim frequency
- event mismatch
- inconsistent rider activity patterns

### 3. Predictive admin insights
Used to estimate:
- which zones may become high-risk next week
- where claim pressure may rise
- where payout burden is clustering

### Why the AI is practical
We are keeping the models explainable. For this use case, interpretable risk and fraud logic is more valuable than a complex model that is difficult to trust.

---

## Adversarial Defense & Anti-Spoofing Strategy

Param Setu is designed with the assumption that raw GPS can be spoofed. A location ping alone is never treated as proof of presence inside a disruption zone. Instead, the platform uses **multi-signal adversarial validation** to decide whether a claim looks like a genuinely disrupted rider or a coordinated spoofing attempt.

### 1. The Differentiation

The system does not ask only, “Is this rider’s GPS inside the affected zone?”  
It asks, **“Does this rider’s full behavior look like an actually active delivery partner who got disrupted?”**

To answer that, the fraud layer compares:
- claimed location
- recent movement continuity
- app session activity
- shift check-in / check-out behavior
- zone consistency over time
- event timing consistency
- device and network trust signals
- cluster-level coordination patterns across multiple riders

A genuinely stranded rider usually shows a believable pattern: active before the disruption, normal zone history, consistent session behavior, and timing that matches the actual event window.

A spoofing actor usually looks different: sudden location jumps, impossible movement, repeated presence in high-payout zones, weak activity evidence, suspicious device/network patterns, or synchronized claim behavior across many accounts.

### 2. The Data

To detect coordinated fraud, Param Setu looks beyond GPS and analyzes:

**Rider activity signals**
- declared shift window
- app check-in / availability state
- app foreground/background activity near the disruption window
- session duration before and during the event
- policy activation timing versus event timing
- recent operating-zone history

**Movement and spatial consistency signals**
- route continuity over time
- impossible travel jumps
- stationary-at-home patterns while claiming field presence
- repeated appearances in multiple high-risk zones
- mismatch between claimed zone and normal operating pattern

**Device and network trust signals**
- device fingerprint consistency
- emulator / mock-location risk indicators
- repeated claims from linked device patterns
- abnormal IP or network switching during event windows
- suspicious clustering of accounts across similar devices or networks

**Event-consistency signals**
- whether the rider was active before the disruption began
- whether rider availability overlaps the affected shift window
- whether claim timing matches real external event progression
- whether rider behavior changes in a believable way during disruption

**Coordinated-ring signals**
- abnormal claim concentration in the same time window
- synchronized claim attempts from clustered groups
- repeated behavioral or device/network similarities across accounts
- abnormal spikes in new policy activations just before a trigger event

The goal is to detect not just suspicious riders, but suspicious **patterns across riders**.

### 3. The UX Balance

An anti-fraud system should not punish honest workers just because bad weather caused poor connectivity. Param Setu therefore uses a **three-band claim handling model**:

**Low-risk claims**  
Automatically approved when policy, zone, activity, and fraud signals are consistent.

**Medium-risk claims**  
Placed into **soft review**, not rejected immediately. The system falls back to:
- last trusted zone presence
- recent shift check-in state
- app session continuity
- event timing consistency
- rider confirmation inside the app

This protects honest riders during genuine network drops.

**High-risk claims**  
Held for admin review when strong spoofing indicators or coordinated fraud patterns are detected.

### Defense principle

The core rule is simple:

> **No single rider-controlled signal should be enough to unlock payout.**

That means GPS alone is not enough, manual declaration alone is not enough, and app-open state alone is not enough. Payout confidence comes from agreement across behavior, time, zone, device, and event consistency.

This makes Param Setu more resilient against both individual spoofers and organized fraud rings without making the product unfair for honest riders.

---

## Why mobile, not web

We chose a **cross-platform mobile app** because that is where this product actually belongs.

Food delivery riders already work through their phones. Their navigation, shift flow, communication, and earnings tracking all happen on mobile. Asking them to manage income protection from a desktop-first product would be unnatural.

### Why mobile is the right decision
- riders need access during live work shifts
- location-aware validation is easier on mobile
- alerts and payout updates fit mobile better
- onboarding is faster in an app flow
- it matches how gig workers already use digital tools

### Why cross-platform
We are building with **Flutter** so we can move quickly with one codebase across Android and iOS.

The rider experience is mobile-first.  
The admin view can be delivered through a lightweight dashboard.

---

## Tech stack

### Mobile app
- Flutter
- Dart
- Riverpod
- GoRouter
- Supabase Flutter SDK

### Backend
- FastAPI
- Python
- background jobs for trigger monitoring
- REST APIs

### Database / backend platform
- Supabase
- PostgreSQL
- Supabase Auth
- Row Level Security
- Realtime subscriptions

### AI / ML
- Python
- Pandas
- scikit-learn
- anomaly detection for fraud scoring

### Integration capabilities
- weather API
- AQI API
- mobility / access disruption feed
- payout simulation layer
- GPS / location validation
- rider activity validation layer
- simulated delivery platform activity signals

---

```markdown
## High-level architecture

```mermaid
flowchart LR
    A[Flutter Mobile App] --> B[FastAPI Backend]

    B --> C[Supabase Auth]
    B --> D[(Supabase PostgreSQL)]
    B --> E[Supabase Realtime]

    B --> F[Risk Engine]
    B --> G[Fraud Engine]
    B --> H[Trigger Engine]
    B --> I[Payout Simulation Service]

    H --> J[Weather API]
    H --> K[AQI API]
    H --> L[Mobility / Access Disruption Feed]

    G --> M[GPS / Location Validation]
    G --> N[Device and Network Trust Signals]
    G --> O[Rider Activity Validation]

    F --> D
    G --> D
    H --> D
    I --> D

---

## Dashboard metrics

### Worker dashboard

The rider-facing app is designed to show:

- active weekly plan
- insured operating zone
- premium paid this week
- daily protection amount
- claims triggered
- claim reason
- payout status
- payout history
- total earnings protected this week

### Admin dashboard

The admin side is designed to show:

- active policies by zone
- zone-wise risk score distribution
- triggers fired by type
- claims triggered by zone
- suspicious / flagged claims
- payout totals by plan
- exposure concentration by area
- next-week risk outlook
- fraud review queue

This keeps the dashboard aligned with both worker utility and insurer-side operational visibility.

---

## Development plan

We are treating the build in the same order the product needs to work.

### Phase 1 — Foundation

- lock persona and product scope
- define pricing model
- define trigger framework
- design app flow
- define backend services
- document architecture and README

### Phase 2 — Core product

- build rider onboarding flow
- build policy creation flow
- connect Supabase auth and database
- implement weekly premium calculation
- implement trigger monitoring service
- create automated claim flow

### Phase 3 — Intelligence and polish

- add fraud scoring
- add predictive admin metrics
- simulate payout workflow
- improve rider claim visibility
- prepare demo scenario and final presentation

---

## Closing note

Param Setu is our attempt to build something narrow, honest, and actually usable.

The core idea is simple: if external disruption is measurable, then short-term income protection for riders should not depend on slow, manual, traditional claims logic. It should be mobile, lightweight, and responsive to real operating conditions.

That is what we are building.
