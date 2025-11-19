/* Implementa una función para convertir un texto de como parametro de entrada a formato H4CK5R.
 * 
 * Nota: Definimos el formato H4CK5R como uno en el que ocurren las siguiente transformaciones:
 *       - Minusculas -> Mayusculas
 *       - A -> 4
 *       - E -> 5
 *       - O -> 0
 *       - I -> 1
 *       - Espacios -> _ (Barra baja)
 * 
 * Entradas: El texto a convertir.
 * Salidas: El texto introducido en formato H4CK5R.
 * 
 * Ejemplos:
 * 	 - ines -> 1N3S
 * 	 - Jor ge -> J0R_G5
 * 	 - d a n i -> D_4_N_1
 *   
 * Pista 1: Un "switch" puede que ayude...
 * Pista 2: En la tabla ASCII las minusculas estan antes que las mayusculas.
 * */

package pkg;

import java.util.Scanner;

public class Ej4 {
	static String convert(String name) {
		String res = "";
		char curr;
		
		for (int i = 0; i < name.length(); ++i) {
			curr = name.charAt(i);
			
			if (curr >= 'a' && curr <= 'z') {
				curr -= ('a' - 'A');
			}
			
			switch(curr) {
			case 'A':
				res += '4';
				break;
				
			case 'E':
				res += '5';
				break;
				
			case 'O':
				res += '0';
				break;
				
			case 'I':
				res += 1;
				break;
				
			case ' ':
				res += '_';
				break;
				
			default:
				res += curr;
				break;
			}
		}
		
		return res;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String name;
		
		System.out.println("Ejercicio 4:");
		System.out.println();
		
		System.out.print("Introduce un nombre a transformar: ");
		name = in.nextLine();
		
		System.out.println("Nombre en formato H4CK5R: " + convert(name));
	}

}
