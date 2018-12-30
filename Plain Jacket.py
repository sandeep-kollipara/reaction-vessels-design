




from math import ceil

print ("Vessel with plain jacket")


P_int=float(input("Please enter the internal pressure in Nmm-2 : "))
P_ext=float(input("Please enter the external pressure in Nmm-2 : "))
Di=float(input("Enter the internal diameter of the shell in mm : ")) # internal diameter in mm
Pj=1.1*P_ext
Ps=1.1*P_int
CA=float(input("Enter the corrosion allowance in mm : "))# corrosion allowance 
f=[0,96,13.6,70.3] # allowable stress for each material
J=0.85 # joint efficiency
E=[0,190000,69000,112000] # modulus of elasticity for each material
mu=[0,0.3,0.32,0.33] # poisson's ratio for each material

print("Choose a material from the following :\n1. Carbon Steel \n2. Aluminium\n3. Copper\n")
material=int(input())

# Plain Jacket
ts=ceil(Ps*Di/(2*f[material]*J-Ps)) # shell thickness, later we add the corrosion allowance
L_eff=2700.0; # effective jacket length
done=False
n=0
FOS=4 # factor of safety
rings=True
while not done:
    Do=Di+2*ts; # outside diameter in mm
    Pc=(2.42*E[material]*(ts/Do)**2.5)/(((1-mu[material]*mu[material])**0.75)*(L_eff/Do-0.45*((ts/Do)**0.5))) # Critical buckling pressure
    fc=Pc*Do/(2*ts) # critical stress
    Pa=Pc/FOS
    fa=fc/FOS
    if Pa>=Pj and fa<=f[material]: break # if this is satisfied, our thickness is fine

    if rings:
        print("Would you consider the option of stiffening rings? (y/n)")
        if input() in {'Y','y'}:
            n=1 # number of stiffening rings
            while not done:
                Do=Di+2*ts; # outside diameter in mm
                L_eff1=L_eff/(n+1)
                Pc=(2.42*E[material]*((ts/Do)**2.5))/(((1-mu[material]*mu[material])**0.75)*(L_eff1/Do-0.45*((ts/Do)**0.5))) # Critical buckling pressure
                fc=Pc*Do/(2*ts) # critical stress
                Pa=Pc/FOS
                if Pa>=Pj: done=True
                else: n+=1
        else:rings=False
    if not rings: ts+=1 # if thickness is not fine, we increase it and check again
ts_total=ceil(ts+CA) # added corrosion allowance 
tj=Pj*Di/(2*f[material]*J-Pj) # jacket thickness
tj_total=ceil(tj+CA)


# Head 
Rc=2130
W=1.77 # stress intensification factor
th=Ps*Rc*W/(2*f[material]*J)
th_total=ceil(th+CA)

#Bottom
tb=1.67*Pj*Rc*W/(2*f[material]*J)
tb_min=FOS*Rc*3*((1-mu[material]*mu[material])**0.25) * (Pj/(2*E[material]))**0.5
tb_total=ceil(max(tb_min,tb+CA))


print('Shell thickness =',ts_total,'mm')
if rings:
    print('Used',n,'stiffening rings')
print('Jacket thickness =',tj_total,'mm')
print('Head thickness =',th_total,'mm')
print('Bottom plate thickness =',tb_total,'mm')
print('\nAll the above values are including corrosion allowance')

input("Press enter key to exit")



    

