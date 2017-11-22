package org.hierro.exploringdatatypes;

import java.util.Scanner;

public class KgramsToPounds {
	
	public static void main(String[] a){
		Scanner scanner = new Scanner(System.in);
		
		double kilograms;
		double pounds;
		double conversionFactor = 2.20462;
		
		System.out.println("Enter amount of Kilograms: ");
		kilograms = scanner.nextDouble();
		
		pounds = kilograms * conversionFactor;
		
		System.out.println(pounds);
	}

}
