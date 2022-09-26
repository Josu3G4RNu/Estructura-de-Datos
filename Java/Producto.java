public class Producto {
    public static int calcularProducto(int[] v, int b, int indice) {
        if(indice < 0){
            return 1;
        }else {
            if (v[indice] > b){
                return v[indice] * calcularProducto(v,b,indice-1);
            } else {
                return calcularProducto(v,b,indice-1);
            }
        }
    }

    public static void main(String[] args) {
        int[] v = new int[]{1, 3, 5, 7, 9};
        System.out.println(calcularProducto(v,4,v.length-1));
    }
}