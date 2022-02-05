/*
 * Algorithms and Complexity                              February 05, 2022
 * IST 4310
 * Prof. M. Diaz-Maldonado
 *
 * Synopsis:
 * Solves the summation problems: 1.3.5-7a, 1.3.5-7e, and 1.3.5-7f.
 *
 *
 * Copyright (c) 2022 Misael Diaz-Maldonado
 * This file is released under the GNU General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *
 * References:
 * [0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007.
 *
 */

class Summations
{
	public static void main (String[] args)
	{

		/* Problem 1.3.5-7a: for i=[1, N+1), sum(3*i+7) */
		int N = 16;	// end-value of the summation

		int isum = 0;
		int iexact = 3 * (N*(N+1)/2) + 7 * N;
		for (int i = 1; i != (N+1); ++i)
			isum += 3 * i + 7;


		System.out.println("\n\n");
		System.out.println("Problem 1.3.5-7a:");
		System.out.printf ("exact:   %d\n", iexact);
		System.out.printf ("numeric: %d\n", isum);
		System.out.println("\n\n");


		/* Problem 1.3.5-7e: for i=[1, N+1), sum(6^i) */
		N = 15;

		double A = 6.0;
		double sum = 0;
		double exact = (Math.pow(A, N+1) - 1.0) / (A - 1.0) - 1.0;
		for (int i = 1; i != (N+1); ++i)
			sum += Math.pow(A, i);


		System.out.println("Problem 1.3.5-7e:");
		System.out.printf ("exact:   %f\n", exact);
		System.out.printf ("numeric: %f\n", sum);
		System.out.println("\n\n");


		/* Problem 1.3.5-7f: for i=[7, N+1), sum(4^i) */
		N = 15;

		A = 4.0;
		sum = 0;
		exact = (Math.pow(A, N+1) - 1.0) / (A - 1.0) -
			(Math.pow(A, 7.0) - 1.0) / (A - 1.0);
		for (int i = 7; i != (N+1); ++i)
			sum += Math.pow(A, i);


		System.out.println("Problem 1.3.5-7f:");
		System.out.printf ("exact:   %f\n", exact);
		System.out.printf ("numeric: %f\n", sum);
		System.out.println("\n\n");
	}
}
