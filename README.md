# ShiftSure
### AI-Powered Weekly Income Protection for Food Delivery Riders

ShiftSure is a hyperlocal AI-powered parametric income protection platform for urban food delivery riders. It dynamically prices weekly coverage, monitors external disruption signals such as heavy rain, flooding, extreme heat, severe pollution, and access restrictions, detects suspicious claims using AI, and automatically simulates payouts for lost earnings.

---

## Problem Statement

Platform-based food delivery riders are critical to India’s urban economy, but their earnings remain highly vulnerable to uncontrollable external disruptions. Events such as heavy rainfall, waterlogging, extreme heat, severe air pollution, and sudden road or zone restrictions can sharply reduce their active delivery hours and cause immediate income loss. Existing protection systems do not address this short-term income volatility in a practical, accessible, and worker-friendly way.

ShiftSure solves this problem through a **parametric insurance model** designed specifically for food delivery riders. Instead of asking workers to submit lengthy manual claims, the platform continuously monitors predefined external conditions. When those conditions cross a payout threshold in the worker’s insured operating zone, the system automatically identifies eligibility, validates activity and location consistency, and initiates a simulated payout.

This solution is intentionally designed around the hackathon’s required constraints:
- coverage is strictly limited to **income loss**
- no health, life, accident, or vehicle-repair protection is included
- pricing is structured on a **weekly basis**
- AI is used for **risk assessment**, **fraud detection**, and **predictive analytics**
- claims are triggered through **parametric external events** rather than traditional manual documentation

---

## Why This Matters

Food delivery riders work in a highly variable, shift-based earning environment. A single day of disruption during peak lunch or evening windows can materially affect weekly take-home income. However, traditional insurance products are not designed for this type of short-cycle, hyperlocal, operational risk.

ShiftSure introduces a more practical model:
- **low-friction weekly premiums**
- **hyperlocal risk-based pricing**
- **zero-touch claims**
- **fast simulated payouts**
- **clear transparency for both workers and insurers**

---

## Persona Focus

### Primary Persona
**Urban food delivery riders in Chennai working for platforms such as Swiggy and Zomato**

### Why This Persona
We deliberately narrowed our scope to a specific and operationally realistic user segment rather than attempting to solve for all gig workers at once.

This persona is strong because:
- food delivery riders are directly exposed to outdoor disruption risk
- Chennai provides a strong real-world context for weather, flooding, heat, and pollution-related earning disruptions
- the relationship between disruption and lost earnings is easy to explain and demonstrate
- the weekly earning cycle maps well to a weekly premium model

### Example Persona
**Rahul**, a 24-year-old Swiggy delivery rider in Chennai, works lunch and evening shifts. His earnings depend on completing enough deliveries during a small number of high-value working windows. During heavy rain, severe heat, or flooded road conditions, he may lose multiple productive hours in a single day. ShiftSure protects his income during these uncontrollable events.

---

## Our Solution

ShiftSure is a **web-first AI-enabled parametric income protection platform** built for food delivery riders.

The system:
1. onboards the rider with basic profile and operating-zone data
2. generates a risk score using AI
3. recommends a weekly premium and coverage slab
4. continuously monitors external disruption signals
5. automatically creates a claim when the disruption threshold is crossed
6. runs fraud checks before approval
7. simulates instant payout
8. provides dashboards for both workers and insurer/admin users

---

## Why Parametric Insurance

Traditional insurance relies on manual filing, documentation, and delayed claim investigation. That model is too slow and too operationally heavy for gig workers who need rapid short-term income continuity.

ShiftSure uses a **parametric insurance approach**, where payouts are triggered by predefined measurable conditions rather than manual damage assessment.

Examples:
- rainfall exceeds a threshold in the rider’s delivery zone
- AQI crosses a severe threshold
- heat index reaches unsafe outdoor-work levels
- road access or zone restrictions block normal delivery activity

This allows the platform to automate protection in a way that feels immediate, transparent, and scalable.

---

## Core Features

### 1. AI-Powered Risk Assessment
ShiftSure calculates a worker-specific weekly risk score based on:
- operating zone
- historical weather severity
- flood/waterlogging exposure
- extreme heat exposure
- pollution exposure
- disruption frequency
- shift pattern
- approximate earnings band

This risk score drives:
- premium recommendation
- coverage slab recommendation
- portfolio risk segmentation

### 2. Dynamic Weekly Pricing
Unlike traditional annual or monthly plans, ShiftSure is intentionally designed around the weekly earning cycle of gig workers. Pricing is recalculated through a weekly model to remain affordable, explainable, and aligned with short-cycle income patterns.

### 3. Parametric Trigger Monitoring
The platform continuously checks external disruption signals and evaluates whether a worker’s insured zone has crossed a payout threshold.

### 4. Automatic Claims
When the system detects a valid disruption affecting an insured worker’s zone, the claim is automatically initiated without requiring the worker to manually submit paperwork.

### 5. AI-Based Fraud Detection
ShiftSure applies fraud checks such as:
- GPS mismatch with registered operating zone
- duplicate claims for the same event window
- abnormal claim frequency
- event-to-activity inconsistency
- suspicious movement patterns

### 6. Instant Payout Simulation
Approved claims are routed to a mock payout engine to simulate how a worker would receive compensation through a digital payment flow.

### 7. Dual Dashboards
The platform includes:
- a **worker dashboard** showing active coverage, protected earnings, and payout history
- an **admin dashboard** showing risk distribution, exposure, fraud alerts, loss ratios, and predictive claim insights

---

## Parametric Trigger Framework

We designed ShiftSure around five core disruption classes that directly affect a food delivery rider’s ability to earn.

### Trigger 1: Heavy Rain
**Condition:** rainfall intensity crosses the defined threshold in the rider’s active zone  
**Example threshold:** rainfall > 80 mm in a defined time window  
**Impact:** rider cannot safely operate outdoors

### Trigger 2: Flood / Waterlogging
**Condition:** flood severity or waterlogging risk crosses the defined threshold  
**Impact:** roads become inaccessible and deliveries are disrupted

### Trigger 3: Extreme Heat
**Condition:** temperature or heat index exceeds safe outdoor delivery thresholds  
**Impact:** working conditions become unsafe and active hours fall

### Trigger 4: Severe Air Pollution
**Condition:** AQI exceeds a severe-risk threshold  
**Example threshold:** AQI > 400  
**Impact:** extended outdoor work becomes unsafe

### Trigger 5: Access Restriction / Mobility Disruption
**Condition:** sudden road closure, zone restriction, curfew, or severe traffic blockade  
**Impact:** pickup/drop routes become inaccessible

---

## Trigger Logic

A worker becomes eligible for claim creation when all of the following are true:

- disruption threshold is breached
- policy is active
- worker’s operating zone matches the affected zone
- fraud score is below rejection threshold

### Disruption Severity Index
To make trigger handling more robust, ShiftSure uses a combined disruption score:

`DSI = Weather Score + Environmental Score + Mobility Score`

Where:
- **Weather Score** captures rainfall, flooding, and heat severity
- **Environmental Score** captures AQI severity
- **Mobility Score** captures road restriction, closure, or congestion severity

If the **Disruption Severity Index** crosses a configured threshold, the worker becomes eligible for automated claim evaluation.

---

## Weekly Pricing Model

The weekly pricing model is designed to match the short earning cycle of delivery riders while preserving affordability and explainability.

### Base Plans

| Plan | Weekly Premium | Daily Income Protection | Ideal User Segment |
|------|----------------|-------------------------|--------------------|
| Basic | ₹19/week | up to ₹250/day | Low-risk zones |
| Standard | ₹29/week | up to ₹400/day | Medium-risk zones |
| Plus | ₹45/week | up to ₹600/day | High-risk zones |

### AI-Based Premium Adjustment
The final weekly premium is adjusted using an AI-generated risk score.

#### Inputs
- zone-level disruption history
- rainfall risk
- flooding frequency
- heat exposure
- AQI severity
- worker shift pattern
- operating intensity
- approximate earnings band

#### Outputs
- risk score (0–100)
- recommended plan
- premium adjustment
- suggested protection band

### Example Hyperlocal Pricing
- low-risk zone rider → ₹22/week
- flood-prone zone rider → ₹38/week
- high heat + high pollution corridor rider → ₹34/week

This gives us a strong differentiator: **hyperlocal risk-based weekly pricing**, rather than city-wide flat premiums.

---

## AI Architecture

ShiftSure uses AI in three distinct layers.

### A. Risk Scoring Engine
This engine predicts the likelihood of disruption-driven income loss for a worker.

**Inputs**
- operating zone
- historical weather patterns
- flood exposure
- AQI history
- heat risk
- shift timing and work pattern

**Outputs**
- risk score
- premium recommendation
- protection slab recommendation

### B. Fraud Detection Engine
This engine detects suspicious claim behavior.

**Signals**
- GPS mismatch
- duplicate event-window claims
- abnormal claim frequency
- impossible activity patterns
- mismatch between claimed zone and disruption zone

**Outputs**
- fraud risk score
- approve / flag / reject suggestion

### C. Predictive Operations Engine
This engine supports the admin dashboard with forward-looking operational intelligence.

**Outputs**
- next week’s high-risk zones
- expected claim load
- expected payout burden
- zone-wise exposure hotspots
- emerging loss-ratio concerns

This layered AI architecture helps ShiftSure look less like a simple app and more like an insurtech decision platform.

---

## System Workflow

### Worker Flow
1. rider signs up and enters basic profile information
2. platform, city, operating zone, and earnings band are captured
3. AI risk engine generates a worker risk score
4. system recommends weekly premium and coverage
5. worker activates policy
6. trigger engine continuously monitors disruption signals
7. if a valid event affects the rider’s insured zone, a claim is automatically created
8. fraud engine validates consistency
9. payout engine simulates instant compensation
10. rider sees the payout reason and protected earnings summary

### Admin Flow
1. monitor active policies
2. view zone-level exposure
3. track live disruption events
4. review fraud alerts
5. analyze claim trends
6. monitor expected next-week risk and payout burden

---

## Platform Choice: Why Web First

We chose a **web-first platform** for the hackathon phase because:
- it is faster to prototype and demonstrate
- it supports both worker and admin experiences in one product
- it is better suited for analytics dashboards
- it reduces development friction during the early build stage

In a real-world product, ShiftSure can later expand to a mobile-first worker experience. For the hackathon, web-first gives the best balance between speed, clarity, and demo quality.

---

## System Architecture

### High-Level Architecture

```text
Worker Web App / Admin Dashboard
            │
            ▼
         API Gateway
            │
 ┌──────────┼──────────┐
 ▼          ▼          ▼
Worker   Policy     Claim Service
Service  Service        │
            │           ▼
            ▼      Fraud Engine
        Risk Engine      │
            │           ▼
            └────► Trigger Engine
                        │
                        ▼
                External APIs / Mock Feeds
         (Weather, AQI, Mobility, Curfew, Payout)
