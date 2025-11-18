/* Dada una lista de la compra de 5 productos calcula el precio total del carro de la compra.
 *
 * Nota: Precio de los alimentos:
 * 		   - Agua               1€
 *         - CocaCola           2,50€
 * 		   - Pizza Tarradellas  17,30€
 *         - Bandeja de merluza 30,99€
 * 
 * Entradas: El nombre de los alimentos, **¡recuerda validar las entradas!**.
 * Salidas: El precio total del carro de la compra.
 * 
 * Ejemplos:
 *   - Agua, CocaCola, Pizza Tarradellas, Bandeja de merluza, Agua -> 52.79€
 *   - Agua, Agua, CocaCola, CocaCola, Agua                        ->  8.00€
 * */

package pkg;

import java.util.Scanner;

public class Ej2 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String curr = "";
		double total = 0;
		
		System.out.println("Ejercicio 2:");
		System.out.println();
		
		for (int i = 0; i < 5; ++i) {
			System.out.print("Introduzca el nombre de un alimento: ");
			curr = in.nextLine();
			
			switch (curr) {
			case "Agua":
				total++;
				break;
				
			case "CocaCola":
				total += 2.5;
				break;
				
			case "Pizza Tarradellas":
				total += 17.30;
				break;
				
			case "Bandeja de merluza":
				total += 30.99;
				break;
				
			default:
				System.out.println("¡Alimento desconocido!, ignorando...");
				break;
			}
		};
		
		System.out.println();
		System.out.println("Precio total del carro de la compra: " + total + "€");
	}

}
