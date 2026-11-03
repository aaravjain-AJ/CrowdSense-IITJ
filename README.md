# CrowdSense-IITJ
Real-Time Campus Crowd Telemetry, Predictive Visit Recommendations, and Accessible Indoor-Outdoor Wayfinding for Students, Elderly Visitors, and Persons with Disabilities at IIT Jodhpur
# CrowdSense IIT Jodhpur (CrowdSense-IITJ)

**Real-Time Campus Crowd Telemetry, Predictive Visit Recommendations, and Accessible Indoor-Outdoor Wayfinding for Students, Elderly Visitors, and Persons with Disabilities (PwD)**

Inspired by digital campus wayfinding and IoT occupancy platforms such as MazeMap (https://www.mazemap.com/), **CrowdSense IITJ** is purpose-built for the 852-acre IIT Jodhpur Campus in Karwar, Rajasthan.

Imagine opening CrowdSense before walking across campus to the Library, Dining Hall, or Sports Complex. At a glance, it tells you:
- **The Learning Hub (Central Library)**: **Less crowded** (21% occupancy | 0 min wait | 38 dB quiet zone) — *Ideal to visit right now*
- **Central Dining Hall (Veg & Non-Veg Mess)**: **Very crowded** (85% occupancy | ~14 min queue | 76 dB) — *Best time to visit: 02:00 PM – 03:00 PM or 09:00 PM*
- **Indoor & Outdoor Sports Complex**: **Moderately crowded** (54% occupancy | ~4 min wait | 62 dB) — *Best time to visit: 03:00 PM – 04:00 PM or 06:00 AM*

Beyond student convenience, CrowdSense integrates **100% step-free wheelchair A* routing**, **low-exertion shaded pathways with rest benches for elderly visitors**, **ambient acoustic/sensory load monitoring**, **WCAG AAA High-Contrast & Audio Readout (TTS)**, and **one-tap campus E-Rickshaw / priority seating reservation**.

## Key Features by Target User Group

| Target Group | Core Challenges at IIT Jodhpur | CrowdSense IITJ Assistive Capabilities |
| :--- | :--- | :--- |
| **Students** | Long queues at the Three-Storied Dining Building during peak lunch (12:15–2:30 PM) and dinner (8:00–10:00 PM); finding free study desks at The Learning Hub or courts at the Sports Complex. | Live crowd badges (**Less crowded**, **Moderately crowded**, **Very crowded**), floor-by-floor occupancy breakdown, and predictive **Best Time to Visit** windows. |
| **People with Disabilities (PwD)** | Navigating stairs vs. ramps, checking if building elevators are operational in Hostels and the Dining Hall, finding wheelchair bays in the Lecture Hall Building (LHB), and avoiding sensory overload. | **100% Step-Free Wheelchair A* Routing**, live elevator & accessible restroom status, **Sensory-Safe Quiet Mode** (dB monitoring), **WCAG AAA High-Contrast UI**, and **Web Speech API Voice Readout (TTS)**. |
| **Elderly People (Parents, Senior Faculty & Staff)** | Walking 300–600m in high Jodhpur temperatures, standing in long queues at the Mess or Primary Health Centre OPD, and locating shaded rest benches. | **Elderly Low-Exertion Shaded Routing** along IITJ's landscaped berms and pergolas with rest-bench waypoints, **Zero-Wait OPD / Priority Mess Counter alerts**, and **One-Tap E-Rickshaw Shuttle Dispatch**. |

## Repository Structure
- `backend/main.py` — FastAPI REST server for live crowd telemetry, predictive visit windows, accessible A* campus routing, and E-Rickshaw / priority seat reservations.
- `backend/forecaster.py` — Crowd classification (`Less crowded`, `Moderately crowded`, `Very crowded`) and profile-aware Best-Time recommender.
- `backend/routing.py` — Multi-profile Weighted A* Accessible Campus Router (`standard`, `wheelchair`, `elderly`, `sensory_safe`).
- `backend/seed_data.py` — Grounded IIT Jodhpur facility dataset (Library, Mess, Sports Complex, Lecture Hall Building, Primary Health Centre, Shamiyana Cafe) and campus pedestrian graph.
- `edge_estimator/sensor_fusion.py` — Privacy-preserving Wi-Fi AP probe count + overhead gate YOLOv8 headcount + acoustic dB sensor fusion simulator.
- `frontend/src/App.jsx` & `crowdsense_iitj_app.html` — Interactive dashboard, 24-hour forecast charts, SVG campus wayfinder, and assistive tools.
- `docs/SUBMISSION_REPORT.md` — Complete technical report and 4-student team module breakdown.

## Quick Start
```bash
pip install -r backend/requirements.txt
python3 -m unittest backend/tests/test_api.py -v
uvicorn backend.main:app --reload --port 8000
python3 edge_estimator/sensor_fusion.py --steps 20
```
