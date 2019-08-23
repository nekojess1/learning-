package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {

	    Scanner ler = new Scanner(System.in);
        int number = ler.nextInt();
        if (number < 0){
            System.out.println("NEGATIVO");
        }
        else{
            System.out.println("NAO NEGATIVO");
        }

    }
}
