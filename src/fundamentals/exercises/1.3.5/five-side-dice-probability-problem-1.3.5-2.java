/*
 * Algorithms and Complexity                              February 05, 2022
 * IST 2048
 * Prof. M. Diaz-Maldonado
 *
 * Synopsis:
 * Uses a Binary Search Tree BST to solve the five-side dice problem
 * 1.3.5-2. Generates a table of possible outcomes (total of the dice pair)
 * and their respective probabilities.
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
 * [1] maps: www.javatpoint.com/java-map
 *
 */

import java.util.Map;
import java.util.TreeMap;

class FiveSideDiceProbabilityProblem
{
	public static void main (String[] args)
	{

		// creates tree
		Map<Integer,Integer> tree = new TreeMap<Integer,Integer>();

		int n = 0;
		// initializes tree with zeroes
		for (int i = 1; i != 6; ++i)
		{
			for (int j = 1; j != 6; ++j)
			{
				tree.put(i+j, 0);
				++n;
			}
		}


		// counts number of instances
		for (int i = 1; i != 6; ++i)
		{
			for (int j = 1; j != 6; ++j)
				tree.replace(i+j, (tree.get(i+j)+1));
		}


		/* tabulates results */
		System.out.println("\n\n");
		System.out.println("Five-Side Dice Probability Problem\n");
		System.out.printf("number of possible outcomes: %d\n\n",n);
		System.out.println(
			"outcome    repetitions    probability"
		);
		System.out.println(
			"-------------------------------------"
		);


		double p = 0;	// accumulates the total probability
		for (Map.Entry t:tree.entrySet())
		{
			System.out.printf(
				"%4d         %4d        %8.2f\n",
				t.getKey(), t.getValue(),
				( (int) t.getValue() ) / ( (float) n)
			);

			p += ( (int) t.getValue() ) / ( (float) n);
		}

		System.out.println("\n\n");
		System.out.printf ("total probability: %f\n", p);
		System.out.println("\n\n");


	}
}
