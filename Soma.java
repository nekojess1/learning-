package uri;

import java.util.Locale;


import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		
		double n = 3.14159;
		double raio = sc.nextDouble();
		double resultado = n*Math.pow(raio,2);
		
		System.out.printf("A=%.4f\n",resultado);
		
	    sc.close();
	}
}
