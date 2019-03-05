#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    printf("************************************\n");
    printf("* Bem-vindo ao Jogo da Adivinhação *\n");
    printf("************************************\n");
		
		printf("As regras são simples: \n");
		printf("* O jogo irá pensar em um número aleatório de 0 - 100.\n");
		printf("* O jogador começa com 1000 pontos e perde pontos conforme o número chutado.\n");
		printf("  - Exemplo: chute = 45, número pensado = 15, ou seja 45 - 15 = -30 pontos.\n");
		printf("    Observação: Não será mostrado quantos pontos foram perdidos.\n");
		printf("* O jogo acaba quando o jogador acertar o número ou zerar os seus pontos\nTenha um bom jogo e vamos começar!\n\n");

    int jogo = 1;

    int resposta;
    int numerosecreto;
    int chute;
    int tentativas;
    int pontos;

    while (jogo) {
      srand(time(0));
      numerosecreto = rand() % 100;
      tentativas = 1;
      pontos = 1000;

      while (pontos > 0) 
      {
        printf("Digite um número: ");
        scanf("%d", &chute);

        if (chute < 0)
        {
          printf("Não é permitido chutes com números negativos.\n");
          continue;
        }

        if (chute == numerosecreto)
        {
          printf("Parabéns! Voce acertou na tentativa %d\n", tentativas);
          break;
        }
        else if (chute < numerosecreto)
        {
          printf("Seu chute foi menor que o número secreto.\n");
        }
        else
        {
          printf("Seu chute foi maior que o número secreto.\n");
        }
        pontos = pontos - chute;
        tentativas++;
      }
      
      if (pontos <= 0)
      {
          printf("Gamer Over!\n");
          printf("O número correto é: %d\n", numerosecreto);
          printf("Você terminou o jogo com %d pontos\n", pontos);
      }
      else{
        printf("Você terminou o jogo com %d pontos\n", pontos);
      }

      printf("Obrigado por jogar!\n\n");
      printf("Para jogar novamente digite 1 ou para sair digite 0\n");
      printf("Resposta: ");
      scanf("%d", &resposta);

      jogo = resposta;
    }
}
