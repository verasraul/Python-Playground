package org.hierro.exploringdatatypes;

import java.util.Scanner; //For Scanner

public class ExploreDataTypes {


	 public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		 /* declarations */
		int wholenumA=100;  /* 100 is an integer constant. */
		int wholenumB=-37;
		float realnum;
		char letter;
		
		/* Assign values.  */
		realnum=3.14f;  /* This is an assignment.
	    3.14 is a double constant. */
		letter='M';
	
		System.out.printf("A whole number goes here: %d", wholenumA); /*C Format*/
//		System.out.println("A whole number goes here: "+wholenumA); /*Java Format - Can you convert the rest to Java Format?*/
		
		System.out.printf("Backslash n advances to a new line.\n");
		System.out.printf("Several lines\nin one printf\nis possible\n");
		System.out.printf("Two of the same: %d %d, and one different %d.",          
	             wholenumA, wholenumA, wholenumB);
		System.out.printf("\ninteger: %d, real number: %f, character: %c\n", 
	             wholenumA, realnum, letter);
		
		/* Obtaining data from the keyboard. */
		System.out.printf("Enter an integer then press <enter>.  ");
		wholenumA = scanner.nextInt();/* Replaces the value in 
	                                 wholenumA. Notice the & */
		System.out.printf("Great!  You entered %d\n",wholenumA);
		System.out.printf("Enter a real number, then press <enter>.");
		realnum = scanner.nextFloat();
		System.out.printf("Enter a character, then press <enter>.");   /*The 
	             character should not be in quotes.*/
		letter = scanner.next().charAt(0);
		System.out.printf("The letter is %c and the realnumber was %f\n", 
	             letter, realnum);
		
		scanner.close();//ALWAYS CLEAN UP YOUR MESS
	}

}
