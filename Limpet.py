




from math import ceil

print("Vessel with limpet coil")

P_int=float(input("Please enter the internal pressure in Nmm-2 : "))
P_coil=float(input("Please enter the coil pressure in Nmm-2 : "))
Di=float(input("Enter the internal diameter of the shell in mm : ")) # internal diameter in mm
di=float(input("Enter the internal diameter of the coil in mm : "))
Pc=1.1*P_coil
Ps=1.1*P_int
CA=float(input("Enter the corrosion allowance in mm : "))# corrosion allowance 
f=[0,96,13.6,70.3] # allowable stress for each material
J=0.85 # joint efficiency
E=[0,190000,69000,112000] # modulus of elasticity for each material
mu=[0,0.3,0.32,0.33] # poisson's ratio for each material

print("Choose a material from the following :\n1. Carbon Steel \n2. Aluminium\n3. Copper\n")
material=int(input())

ts=ceil(Ps*Di/(2*f[material]*J-Ps)) # shell thickness, later we add the corrosion allowance
ts_total=ceil(ts+CA) # added corrosion allowance 



tc=ceil(Pc*di/(2*f[material]))

fps=Ps*Di/(2*ts)+Pc*di/(4*tc+2.5*ts)
fas=Ps*Di/(4*ts)+Pc*di/(2*ts)+2*(Pc-Ps)*(di+2*tc)**2/(3*ts*ts)
while fps>f[material] or fas>f[material]:
    tc+=1
    fps=Ps*Di/(2*ts)+Pc*di/(4*tc+2.5*ts)
    fas=Ps*Di/(4*ts)+Pc*di/(2*ts)+2*(Pc-Ps)*(di+2*tc)**2/(3*ts*ts)
tc_total=max(3,tc+CA)




print('Shell thickness =',ts_total,'mm')
print('Coil thickness =',tc_total,'mm')


    

input("Press enter key to exit")