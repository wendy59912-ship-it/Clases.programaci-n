public class Main {
    public static void main(String[] args) {
        String[] casosDePrueba = {
            "(a+b)*[c-d]",        
            "{[(a+b)*c]-d}",      
            "(a+b]",              
            "(a+b))",             
            "((a+b)",             
            "{(a+b]}"             
        };
        System.out.println("==================================================");
        System.out.println("  ANALIZADOR SINTÁCTICO DE EXPRESIONES (PILA LIFO)");
        System.out.println("==================================================\n");

        for (int i = 0; i < casosDePrueba.length; i++) {
            String expresion = casosDePrueba[i];
            boolean esValida = AnalizadorSintactico.evaluarExpresion(expresion);

            System.out.println("Caso " + (i + 1) + ": " + expresion);
            if (esValida) {
                System.out.println("Resultado: Expresión sintácticamente VÁLIDA.");
            } else {
                System.out.println("Resultado: Expresión sintácticamente INVÁLIDA.");
            }
            System.out.println("--------------------------------------------------");
        }
    }
}
