package banco;

import javax.swing.JOptionPane;

public class main {

	public static void main(String[] args) {

		int autenticado = 0;
		int tentativaSenha = 0;
		String senhaCorreta = "senai123";
		String senhaDigitada = "";
		int loopSenha = 0;
		int opcao = 0;
		float saldo = 500f;
		float valor = 0f;
		float deposito = 0f;
		

		JOptionPane.showMessageDialog(null, "Bem vindo ao Banco", "Bem Vindo", JOptionPane.INFORMATION_MESSAGE);

		while (loopSenha == 0) {
			senhaDigitada = JOptionPane.showInputDialog(null, "Digite sua senha:", "Auth", JOptionPane.WARNING_MESSAGE);

			if (senhaCorreta.equals(senhaDigitada)) {
				autenticado = 1;
				loopSenha = 1;
				JOptionPane.showMessageDialog(null, "Usuario autenticado com sucesso", "Sucesso",
						JOptionPane.INFORMATION_MESSAGE);

			} else {
				tentativaSenha++;
				if (tentativaSenha >= 3) {
					JOptionPane.showMessageDialog(null, "Bloqueado!", "Erro!", JOptionPane.ERROR_MESSAGE);
					loopSenha = 1;
				} else {
					JOptionPane.showMessageDialog(null, "Senha Incorreta, tentativa:" + tentativaSenha, "Erro!",
							JOptionPane.ERROR_MESSAGE);
				}
			}
			while (autenticado == 1) {
				opcao = Integer.parseInt(JOptionPane.showInputDialog(null,
						"Escolha a opcao desejada:\n" + "1-Saldo\n2-Saque\n3-Deposito\n" + "4-Encerrar", "Sua conta",
						JOptionPane.INFORMATION_MESSAGE));
				switch (opcao) {
				case 1: {
					JOptionPane.showMessageDialog(null, "seu saldo �:" + saldo, "saldo",
							JOptionPane.INFORMATION_MESSAGE);
				}
					break;
				case 2: {
					valor = Float.parseFloat(JOptionPane.showInputDialog(null,
							"Seu saldo �: R$" + saldo + "\nDigite o valor a ser sacado:", "Sua conta",
							JOptionPane.INFORMATION_MESSAGE));
					if (valor > saldo) {
						JOptionPane.showMessageDialog(null, "Saldo Insuficiente!", "Erro!", JOptionPane.ERROR_MESSAGE);
					} else {
						saldo = saldo - valor;
						JOptionPane.showMessageDialog(null, "Saque efetuado com sucesso!", "Sucesso!",
								JOptionPane.INFORMATION_MESSAGE);
						}
					}
					break;
				case 3:{
					deposito = Float.parseFloat(JOptionPane.showInputDialog(null, "Deposito: R$" + deposito + "\nDigite o valor a ser Depositado:" , "Sua conta",
							JOptionPane.INFORMATION_MESSAGE));
					} 
					break;
				case 4:{
					JOptionPane.showMessageDialog(null, "Fechando Agora!", "Saindo!", JOptionPane.INFORMATION_MESSAGE);
					autenticado = 0;
					break;
					}
				}
			}
		}
	}
}
