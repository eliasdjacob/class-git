package leccion2;

import java.util.Scanner;

public class Leccion2 {

    public static void main(String[] args) {
        /*var condicion = true;
        if(!condicion){
            System.out.println("La condicion es verdadera: " + condicion);
        }else{
            System.out.println("La condicion es falsa: " + condicion);
        }

        var numero = 9;
        var numeroTexto = "numero desconocido";
        if (numero == 1) {
            numeroTexto = "numero 1";
        } else if (numero == 2) {
            numeroTexto = "numero 2";
        } else if (numero == 3) {
            numeroTexto = "numero 3";
        } else if (numero == 4) {
            numeroTexto = "numero 4";
        } else {
            numeroTexto = "numero no encontrado";
        }
        System.out.println("Numero texto = " + numeroTexto);
         */
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "numero 1";
                break;
            case 2:
                numeroTexto = "numero 2";
                break;
            case 3:
                numeroTexto = "numero 3";
                break;
            case 4:
                numeroTexto = "numero 4";
                break;
            default:
                numeroTexto = "numero no encontrado";
                break;
        }
        System.out.println("El numero texto es igual a: " + numeroTexto);
    }

}
