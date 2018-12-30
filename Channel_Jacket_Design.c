#include <stdio.h>
#include <math.h>

void main(){
	float pext, pint, Di, dch, f1, f2, ca, ts, tch;
	float fp, fps, fas, fa, fac, fpc, fb, ts1, ts2;
	float ps, pch, k1, k2, J, tstotal, tchtotal;
	int pod, pod2;
	k1=0.167;
	k2=0.12;
	J=0.85;
	printf("Channel Jacket Design Program\n");
	pod=0;
	while(pod!=1 && pod!=2 && pod!=3){
		printf("Choose Material of Construction\n1. Carbon Steel (I)\n2. Aluminium Alloy\n3.Copper Alloy\n");
		scanf("%i", &pod);
		if(pod==1){
			f1=f2=95;
			continue;
		}
		else if(pod==2){
			f1=f2=13.6;
			continue;
		}
		else if(pod==3){
			f1=f2=70.3;
			continue;
		}
	}
	printf("Input Corrosion Allowance in mm\n");
	scanf("%f", &ca);	
	printf("Input External Operating Pressure in N/mm2\n");
	scanf("%f", &pext);
	printf("Input Internal Operating Pressure in N/mm2\n");
	scanf("%f", &pint);
	printf("Input Internal Shell Diameter in mm\n");
	scanf("%f", &Di);
	printf("Input Channel Diameter in mm\n");
	scanf("%f", &dch);;
	ps=1.1*pint;
	pch=1.1*pext;
	ts1=(ps*Di)/(2*f1*J-ps);
	ts2=dch*sqrt((k1*pch)/f1);
	if(ts1>=ts2){
		ts=ts1;
	}
	else{
		ts=ts2;
	}
	tch=dch*sqrt((k2*pch)/f2);
	tchtotal=tch+ca;
	if(tchtotal<2){
		tchtotal=2;
		tch=tchtotal-ca;
	}
	else{
	
	}
	pod2=1;
	printf("Results before verification are tch= %.2f, ts=%.2f\n", tch, ts);
	while(pod2){
		printf("The design for selected MoC is being calculated... \n");
		fp=(ps*Di)/(2*ts);
		fac=(pch*dch)/(4*tch+2.5*ts);
		fps=fp+fac;
		if(fps<f1){
			pod2=0;
		}
		else{
			tch++;
		}
	}
	pod2=1;
	while(pod2){
		printf("The design for selected MoC is being calculated... \n");
		fa=(ps*Di)/(4*ts);
		fpc=(pch*dch)/(2*ts);
		fb=(2*(pch-ps)*pow(dch+2*tch,2))/(3*pow(ts,2));
		fas=fa+fpc+fb;
		if(fas<f1){
			pod2=0;
		}
		else{
			tch++;
		}
	}
	tstotal=ts+ca;
	tchtotal=tch+ca;	
	printf("Minimum Acceptable Channel thickness is %.2f", tchtotal);
	printf("mm.\n");
	printf("Minimum Acceptable Shell thickness is %.2f", tstotal);
	printf("mm.\n");
	printf("Press any key to exit.\n");
	scanf("%i", &pod);
}