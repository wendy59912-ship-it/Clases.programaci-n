public class Pila {
    private char[] arreglo;
    private int capacidad;
    private int cima;

    public Pila(int capacidad) {
        this.capacidad = capacidad;
        this.arreglo = new char[capacidad];
        this.cima = -1; 
    }
    public void encolar(char elemento) {
        if (!esLlena()) {
            cima++;
            arreglo[cima] = elemento;
        } else {
            System.out.println("Error: La pila está llena.");
        }
    }
    public char desencolar() {
        if (!esVacia()) {
            char elemento = arreglo[cima];
            cima--;
            return elemento;
        }
        return '\0'; 
    }
    public char obtenerCima() {
        if (!esVacia()) {
            return arreglo[cima];
        }
        return '\0';
    }
    public boolean esVacia() {
        return cima == -1;
    }
    public boolean esLlena() {
        return cima == capacidad - 1;
    }
}