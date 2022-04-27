public class Main {
    public static void main(String[] args) {
        Aviao aviao = new Aviao("Viracopos", "BOEING 737", "Robson", 799.99, 2);
        //System.out.println(aviao.aeroporto);
        //System.out.println(aviao.velocidade);
        //System.out.println(aviao.isCarregado());
        //override string to string
        System.out.println(aviao);
        System.out.println("---------------------------------------------------------------------------------------------");
        Navio navio = new Navio("BH", "Jose", 150, 2000);
        System.out.println(navio);
        System.out.println("---------------------------------------------------------------------------------------------");
        Caminhao ha = new Caminhao();
        ha.definirCaminhao("BR 100", 18, "Jose" );
        System.out.println(ha);
    }
}