# Aerospace-Utility-Toolkit
# aerospace-utils-python

A lightweight Python toolkit for aerospace engineering calculations, atmospheric modeling, and flight telemetry analysis.

## Features

### Rocket Performance

* Tsiolkovsky Rocket Equation (Delta-V)
* Mach Number Calculation
* Dynamic Pressure Calculation
* Reynolds Number Calculation

### Atmospheric Modeling

* ISA (International Standard Atmosphere) temperature profile generation
* Atmospheric layer classification:

  * Troposphere
  * Tropopause
  * Stratosphere

### Telemetry Analysis

* CSV-based flight data processing
* Peak altitude (apogee) detection
* Time-to-apogee calculation
* Flight data export and analysis

---

## Equations

### 1. Tsiolkovsky Rocket Equation

Δv = ve · ln(mt / md)

Where:

* Δv = Total achievable change in velocity (m/s)
* ve = Effective exhaust velocity (m/s)
* mt = Total mass (kg)
* md = Dry mass (kg)

### 2. Mach Number

M = v / a

Where:

* M = Mach Number
* v = Vehicle velocity (m/s)
* a = Local speed of sound (m/s)

Speed of sound:

a = √(γRT)

Where:

* γ = 1.4
* R = 287.05 J/(kg·K)
* T = Temperature (K)

### 3. Dynamic Pressure

q = ½ρv²

Where:

* q = Dynamic pressure (Pa)
* ρ = Fluid density (kg/m³)
* v = Flow velocity (m/s)

### 4. Reynolds Number

Re = (ρvL)/μ

Where:

* Re = Reynolds Number
* ρ = Fluid density (kg/m³)
* v = Flow velocity (m/s)
* L = Characteristic length (m)
* μ = Dynamic viscosity (Pa·s)

---

## Sample Output

==================================================
ROCKET FLIGHT REPORT
====================

Delta-V                  5,632.03 m/s
Mach Number                  2.94
Dynamic Pressure      612,500.00 Pa
Reynolds Number         3.45e+07
================================

---

## Generated Files

### isa_temperature.csv

alt_m,temp_K,layer
0,288.15,Troposphere
500,284.90,Troposphere
1000,281.65,Troposphere

### flight_data.csv

time_s,alt_m,velocity_ms
0,0,0
5,120,50
10,500,120
15,950,140

---

## Usage

Run:

python aerospace_utils.py

Input the required flight and vehicle parameters when prompted.

The program will:

1. Calculate rocket performance metrics
2. Generate ISA atmospheric data
3. Export CSV datasets
4. Analyze flight telemetry
5. Determine apogee and time-to-apogee

---

## Future Roadmap

* Drag force calculations
* Lift calculations
* Specific impulse (Isp)
* Orbital velocity calculator
* Escape velocity calculator
* Multi-stage rocket analysis
* Flight trajectory visualization
* Atmospheric density models
* Max-Q detection
* Flight event detection (liftoff, burnout, apogee, landing)

---

## Educational Purpose

This project is intended for students, hobbyists, and aspiring aerospace engineers who want hands-on experience implementing core aerospace engineering equations in Python.
