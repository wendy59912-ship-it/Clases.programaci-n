public class AnalizadorSintactico {
    public static boolean evaluarExpresion(String expresion) {
        Pila pilaDelimitadores = new Pila(expresion.length());
        for (int i = 0; i < expresion.length(); i++) {
            char caracterActual = expresion.charAt(i);
            if (caracterActual == '(' || caracterActual == '[' || caracterActual == '{') {
                pilaDelimitadores.encolar(caracterActual);
            }   
            else if (caracterActual == ')' || caracterActual == ']' || caracterActual == '}') {
                if (pilaDelimitadores.esVacia()) {
                    return false;
                }
                char apertura = pilaDelimitadores.desencolar();
                if (!esParCompatible(apertura, caracterActual)) {
                    return false;
                }
            }
            
        }  
        return pilaDelimitadores.esVacia();
    }
    private static boolean esParCompatible(char apertura, char cierre) {
        if (apertura == '(' && cierre == ')') return true;
        if (apertura == '[' && cierre == ']') return true;
        if (apertura == '{' && cierre == '}') return true;
        return false;
    }
}
