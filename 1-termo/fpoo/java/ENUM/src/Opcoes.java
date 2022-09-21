public enum Opcoes {
    NAO(9), SIM(1), TALVEZ(99);
    private int num;

    Opcoes(int num){
        this.num = num;
    }

    public int getVal(){
        return num;
    }
}