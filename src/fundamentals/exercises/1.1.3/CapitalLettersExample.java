/*
 * Algorithms and Complexity                                  July 20, 2022
 * IST 4310
 * Prof. M. Diaz-Maldonado
 *
 *
 * Synopsis:
 * Counts the number of capital letters in the GNU General Public License
 * GPL (plain text).
 *
 *
 * Copyright (c) 2022 Misael Diaz-Maldonado
 * This file is released under the GNU General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *
 * References:
 * [0] A Koenig and B Moo, Accelerated C++ Practical Programming by Example
 * [1] JJ McConnell, Analysis of Algorithms, 2nd edition
 *
 */

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileNotFoundException;

class CapitalLettersExample
{
	public static void main (String [] args)
	// reports to user capital letter count of GPL on the console
	{

		// reads GPL and reports capital letter count
		read ();

		// runs tests:
		// test_printASCII();
		return;
	}

	// implementation:
	private static void read ()
	// opens GPL file for reading one character at a time
	{
		String filename = ("GPL.txt");
		File f = new File (filename);
		try
		// the compiler complains if not in a try - catch structure
		{
			// we need a buffer reader to read char-by-char
			FileReader fr = new FileReader (f);
			BufferedReader br = new BufferedReader (fr);
			// reads the buffer one character at a time
			read (br);
		}
		catch (FileNotFoundException e)
		{
			e.printStackTrace();
		}

	}


	private static void read (BufferedReader br)
	/*

	Synopsis:
	Reads buffer one character at a time and reports on the console the
	number of capital letters found.

	*/
	{
		// initializes array index
		int idx = 0;
		// defines lower and upper bounds (ASCII [A, Z])
		int lb = 65, ub = 90;
		// defines offset for incrementing respective counter
		int offset = 65;
		// initializes the capital letter counter array
		int [] counters = initCounters ();

		int c = readBuffer (br);
		while (c != 0xFFFFFFFF)	/* (Note: 0xFFFFFFFF = -1) */
		// reads one character at a time until end-of-file EOF
		{
			// prints the read character on the console
			System.out.printf("%c", c);
			c = readBuffer (br);

			// gets (assumed) index of respective counter
			idx = (c - offset);

			/*

			increments counter if the char is a capital letter

			*/

			if (c >= lb && c <= ub)
				++counters[idx];
		}

		// reports capital letter count on the console
		print (counters);
	}


	private static int readBuffer (BufferedReader br)
	// tries to read a single character from buffer
	{
		int c = 0;
		// the compiler complains if not in a try - catch structure
		try { c = br.read(); }
		catch (IOException e) { e.printStackTrace(); }
		return c;
	}


	private static int [] initCounters ()
	// initializes the capital letter counter array to zero
	{
		int size = 26;	// total number of capital letters [A - Z]
		int [] counters = new int [size];
		for (int i = 0; i != size; ++i)
			counters[i] = 0;

		return counters;
	}


	private static void print (int [] counters)
	// prints the capital letter count on the console
	{
		int c = 0;
		int offset = 65;// Note: when i = 0 we get capital letter A
		int size = 26;	// total number of capital letters [A - Z]
		for (int i = 0; i != size; ++i)
		{
			c = (i + offset);
			System.out.printf("%c: %d\n", c, counters[i]);
		}
	}


	// tests:
	private static void test_printASCII ()
	// prints the capital letters A-Z and the respective ASCII code
	{
		char c;
		int ascii;
		int size = 26;
		int offset = 65;
		for (int i = 0; i != size; ++i)
		{
			ascii = (i + offset);
			c = ( (char) (ascii) );
			System.out.printf("ASCII: %d CHAR: %c\n", ascii, c);
		}
	}
}
