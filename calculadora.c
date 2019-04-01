
    
#include <stdio.h>


/*Programa calculadora*/
/*Comentario nuevo*/


double sumar (double a, double b)

{

    double rsuma;

    rsuma = a + b;

    return rsuma;

}





double restar (double a, double b)

{

    double rresta;

    rresta = a - b;

    return rresta;

}





double multiplicar(double a, double b)

{

    double rmultiplicacion;

    rmultiplicacion = a * b;

    return rmultiplicacion;

}





double dividir(double a, double b)

{

    double rdivision;

    rdivision = a / b;

    return rdivision;

}







int calculadora()

{

    int operacion;

    printf("Indica qué operación quieres realizar");

    printf("\n1. sumar");

    printf("\n2. restar");

    printf("\n3. multiplicar");

    printf("\n4. dividir\n\n");

    scanf("%d", &operacion);

    return operacion;

    

}





int main()

{

    float resultado;

    int x;

    int y;

    int opcioncalc;

    printf("\nIntroduce el primer numero:\n");

    scanf("%d",&x);

    printf("\nIntroduce el segundo numero:\n");

    scanf("%d",&y);

    

    opcioncalc = calculadora();

        if(opcioncalc == 1){

            resultado = sumar(x,y);

        }else if(opcioncalc == 2) {

            resultado = restar(x,y);

        }else if(opcioncalc == 3) {

            resultado = multiplicar(x,y);

        }else if(opcioncalc == 4) {

            resultado = dividir(x,y);

        }





    printf("\nEl resultado es %f \n", resultado);

    return 0;

}


















=======
#include <stdio.h>

double sumar (double a, double b)
{
	double rsuma;
	rsuma = a + b;
	return rsuma;
}

double restar (double a, double b)
{
	double rresta;
	rresta = a - b;
	return rresta;
}

double multiplicar(double a, double b)
{
	double rmultiplicacion;
	rmultiplicacion = a * b;
	return rmultiplicacion;
}

double dividir(double a, double b)
{
	double rdivision;
	rdivision = a / b;
	return rdivision;
}


int calculadora()
{
	int operacion;
	printf("Indica qué operación quieres realizar");
	printf("\n1. sumar");
	printf("\n2. restar");
	printf("\n3. multiplicar");
	printf("\n4. dividir\n\n");
	scanf("%d", &operacion);
	return operacion;
	
}

int main()
{
	float resultado;
	int x;
	int y;
	int opcioncalc;
	printf("\nIntroduce el primer numero:\n");
	scanf("%d",&x);
	printf("\nIntroduce el segundo numero:\n");
	scanf("%d",&y);
	
	opcioncalc = calculadora();
		if(opcioncalc == 1){
			resultado = sumar(x,y);
		}else if(opcioncalc == 2) {
			resultado = restar(x,y);
		}else if(opcioncalc == 3) {
			resultado = multiplicar(x,y);
		}else if(opcioncalc == 4) {
			resultado = dividir(x,y);
		}

	printf("\nEl resultado es %f \n", resultado);
	return 0;
}



