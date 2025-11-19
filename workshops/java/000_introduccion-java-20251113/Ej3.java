/* Toma hasta 100 números enteros positivos, ignora los primos, muestra en pantalla los números recogidos
 * y di cual es el más repetido.
 * 
 * Entradas: Hasta 100 números enteros positivos,
 *           usa el número -1 para indicar el final de la entrada,
 *           **¡recuerda validar las entradas!**.
 * Salidas: Los números recogidos y el más repetido.
 * 
 * Extra 1: Imprime cuantos números han sido ignorados.
 * Extra 2: Calcula la media de los números recogidos.
 * 
 * Ejemplos:
 * 	 - 1, 2, 20, 30, 50, 40, -1 ->
 * 		Números introducidos: 20 30 50 40
 * 		Número más grande: 50
 *
 *   - -1 ->
 * 		Números introducidos:
 * 		Número más grande: 0
 *   
 * Pista:
 *   - Números primos:    2, 3, 5, 73, 97, etc.
 *   - Números no primos: 1, 4, 6, 65, 96, etc.
 * */

package pkg;

import java.util.Scanner;

public class Ej3 {
	static boolean calcIsPrime(int n) {
		boolean isPrime = true;
		
		// Nótese `i = 2 != 0 != 1`.
		for (int i = 2; i < n; ++i) {
			if (n % i == 0) {
				isPrime = false;
			}
		}
		
		return isPrime;
	}
	
	static int findMax(int[] nums) {
		int max = -1;
		
		for (int i = 0; i < nums.length; ++i) {
			if (nums[i] > max) {
				max = nums[i];
			}
		}
		
		return max;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int curr = 0;
		
		final int MAX_NUMS = 100;
		int[] nums = new int[MAX_NUMS];
		
		int n = 0;
		
		// ===== Extra 1 =====
		int total = 0;
		// ===================
		
		// ===== Extra 2 =====
		int sum = 0;
		int average = 0;
		// ===================
		
		System.out.println("Ejercicio 3:");
		System.out.println();
		
		while (curr != -1) {
			System.out.print("Introduzca un número entero positivo (o -1 para final): ");
			curr = in.nextInt();
			
			// ===== Extra 1 =====
			total++;
			// ===================
			
			if (curr > -1 && !calcIsPrime(curr)) {
				nums[n] = curr;
				n++;
			} else if (curr < -1) {
					System.out.println("¡Número introducido negativo!, ignorando...");
			}
		};
		
		System.out.println();
		System.out.println("Números introducidos:");
		System.out.print("  ");
		
		for (int i = 0; i < n; ++i) {
			System.out.print(nums[i] + " ");
			
			// ===== Extra 2 =====
			sum += nums[i];
			// ===================
		}
		
		System.out.println();
		System.out.println();
		
		System.out.println("Número más grande de los aceptados: " + findMax(nums));
		System.out.println();
		
		// ===== Extra 1 =====
		System.out.println("Extra 1: Cantidad de números ignorados: " + (total - n));
		// ===================
		
		// ===== Extra 2 =====
		if (n != 0) {
			average = sum / n;
		}
		
		System.out.println("Extra 2: Media de los números aceptados: " + average);
		// ===================
	}

}
