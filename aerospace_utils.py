import math
import csv

m_t = float(input("What is the total mass of rocket(kg)? "))
m_d = float(input("What is the dry mass of rocket(kg)? "))
v_e = float(input("What is the exhaust velocity of rocket(m/s)? "))
v = float(input("What is the speed of rocket(m/s)? "))
alt_m = float(input("What is the altitude of the rocket(m)? "))
rho = float(input("What is the density of fluid(kg/m^3)? "))
v_f = float(input("What is the flow speed(m/s)? "))
L = float(input("What is the length of specimen(m)? "))
mu = float(input("What is the Dynamic visocity of the fluid(kg/ms)? "))


#1. Tsiolkovsky Equation
def Tsiolkovsky(v_e, m_t, m_d):    # write a function that defines Tsiolkovsky Equation
   
    #Calculate Tsiolkovsky Equation
    return v_e * math.log(m_t/m_d)

# Now call the function we just defined:
delta_V = Tsiolkovsky(v_e, m_t, m_d)

#2.Mach Number
def Mach(v, alt_m):
    T = 288.15 - 0.0065 * alt_m
    c = math.sqrt(1.4 * 287.05 * T)
    return v/c

Mach_Number = Mach(v, alt_m)

#3. Dyanmic Pressure
def dyn_p(rho, v_f):
    return (rho * (v_f ** 2))/2

Dynamic_pressure = dyn_p(rho, v_f)

#4. Reynolds Number
def RN(v_f, rho, L, mu):
    return (rho * v_f * L)/mu

Reynolds_Number = RN(v_f, rho, L, mu)

print("\n╔══════════════════════════════════════════════╗")
print("║            ROCKET FLIGHT REPORT              ║")
print("╠══════════════════════════════════════════════╣")
print(f"║ Delta-V            : {delta_V:>15,.2f} m/s     ║")
print(f"║ Mach Number        : {Mach_Number:>15.2f}         ║")
print(f"║ Dynamic Pressure   : {Dynamic_pressure:>15,.2f} Pa      ║")
print(f"║ Reynolds Number    : {Reynolds_Number:>15,.2f}         ║")
print("╚══════════════════════════════════════════════╝")

import csv
import math

#Generate ISA temperature profile CSV
with open('isa_temperature.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alt_m', 'temp_K', 'layer'])
    for alt in range(0, 50001, 500):
        if alt <= 11000:
            T = 288.15 - 0.0065 * alt
            layer = 'Troposphere' 
        elif alt <= 20000:
            T = 216.65
            layer = 'Tropopause'
        else:
            T = 288.15 - 0.001 * (alt - 20000)
            layer = 'Stratosphere'
        writer.writerow([alt, round(T,2), layer])

print("ISA data written to isa_temperature.csv")

#Generate altitude vs time of peak
peak_altitude = -1
time_of_peak = 0

with open('flight_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_s', 'alt_m', 'vel_ms'])
    
    for t in range (0, 101, 10):
        altitude = -0.5 * ((t-50)**2) + 1250
        velocity = -(t-50) * 10

        if altitude > peak_altitude:
            peak_altitude = altitude
            time_of_peak = t

        writer.writerow([t, altitude, velocity])

print(f"Peak Altitude: {peak_altitude:.2f} m")
print(f"Time of Peak: {time_of_peak:.2f} s")
print("Flight data written to flight_data.csv")
