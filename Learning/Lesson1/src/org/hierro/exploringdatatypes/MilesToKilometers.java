package org.hierro.exploringdatatypes;

import java.util.Scanner;

public class MilesToKilometers {
	final static double KMS_PER_MILE = 1.609;      /* conversion constant       */
	
	public static void main(String[] args) {
		Scanner userInput = new Scanner(System.in);
		double miles;  /* input - distance in miles.       */
		double kms;    /* output - distance in kilometers  */

		/* Get the distance in miles. */
		System.out.printf("Enter the distance in miles> ");
		miles = userInput.nextDouble();

		/* Convert the distance to kilometers. */
		kms = KMS_PER_MILE * miles;

		/* Display the distance in kilometers. */
		System.out.printf("That equals %f kilometers.\n", kms);
//		System.out.println("That equals "+kms+" kilometers.\n");
		
	}

}
