public enum Mensagens {
    BemVindo("Bem vindo"), Saiu("Volte sempre");
    private String msg;


    Mensagens(String msg) {
        this.msg = msg;
    }


    public String getMsg() {
        return msg;
    }    
}