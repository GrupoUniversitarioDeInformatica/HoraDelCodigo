/* Implementar una calculadora de la suma del "juego" para el juego del Mus.
 *
 * Nota: En el Mus se suma el número de cada carta en una mano de 4 con las
 * 		 siguientes excepciones:
 * 		 1. Los treses son reyes.
 * 		 2. Todas las figuras valen 10.
 * 		 3. Los doses valen 1.
 * 
 * Entradas: El valor de cada una de las cuatro cartas, **¡recuerda validar las entradas!**.
 * Salidas: La suma del "juego".
 * 
 * Restricciones: La implementación debe dar uso de al menos un "switch".
 * 
 * Extra: Detectar si las cartas introducidas hacen "juego", es decir, que su suma sea al menos 31.
 * 
 * Ejemplos:
 * 	 - 6,  7,  8, 9 -> 30
 *   - 1,  2,  4, 4 -> 10
 *   - 3, 12, 11, 3 -> 40
 * */

package pkg;

import java.util.Scanner;

public class Ej1 {
	static boolean check(int n) {
		return n >= 1 && n <= 12;
	}
	
	static int getValue(int n) {
		switch(n) {
		case 12:
		case 11:
		case 3:
			return 10;
		case 2:
			return 1;
		default:
			return n;
		}
	}
	
	// Invariantes: Se espera que todos los parámetros sean valores válidos para
	//				la baraja española.
	static int calcSum(int c1, int c2, int c3, int c4) {
		int sum = 0;
		
		sum += getValue(c1);
		sum += getValue(c2);
		sum += getValue(c3);
		sum += getValue(c4);
		
		return sum;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int c1, c2, c3, c4;
		int sum = 0;
		
		System.out.println("Ejercicio 1:");
		System.out.println();
		
		System.out.print("Valor de la carta 1º: ");
		c1 = in.nextInt();
		
		System.out.print("Valor de la carta 2º: ");
		c2 = in.nextInt();
		
		System.out.print("Valor de la carta 3º: ");
		c3 = in.nextInt();
		
		System.out.print("Valor de la carta 4º: ");
		c4 = in.nextInt();
		
		if (check(c1) && check(c2) && check(c3) && check(c4)) {
			sum = calcSum(c1, c2, c3, c4);
			
			System.out.println("La suma para el juego es " + sum);
			
			// ====== EXTRA =====
			if (sum >= 31) {
				System.out.println("Extra: ¡Tienes juego!");
			} else {
				System.out.println("Extra: No tienes juego :(");
			}
			// ==================
		} else {
			System.out.println("¡Alguno de los valores introducidos no es válido para la baraja española!");
		}
	}
}
