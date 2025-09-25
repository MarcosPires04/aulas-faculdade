# Sistema de Saque Bancário em Python

Este projeto é um simples sistema de saque bancário desenvolvido em Python para fins didáticos, durante as aulas da faculdade. O objetivo é simular o funcionamento básico de um caixa eletrônico, com autenticação por senha, opções de saque e saída, emissão de recibo e verificação de saldo.

## Funcionalidades

- **Autenticação por senha**: Solicita ao usuário que insira uma senha para acessar o sistema.
- **Opções de operação**: Permite ao usuário escolher entre realizar um saque ou sair do sistema.
- **Verificação de saldo**: Exibe o saldo atual e verifica se o valor solicitado para saque está disponível.
- **Emissão de recibo**: Pergunta se o usuário deseja imprimir o recibo após o saque.
- **Limpeza de tela**: Utiliza comandos específicos para limpar a tela conforme o sistema operacional.
- **Mensagens interativas**: Exibe mensagens de espera e finalização para melhorar a experiência do usuário.

## Como executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o código em um arquivo com a extensão `.py`, por exemplo: `sistema_saque.py`.
3. Execute o arquivo no terminal/cmd:
   ```bash
   python sistema_saque.py
   ```

## Exemplo de uso

- O sistema irá solicitar a senha do usuário.
- Após a autenticação, é possível escolher entre "saque" ou "sair".
- Se escolher "saque", será solicitado o valor desejado.
- Caso o saldo seja suficiente, o saque será realizado e haverá a opção de imprimir o recibo.
- O saldo final é exibido ao final do processo.

## Estrutura do Código

- **Função `limpar_tela()`**: Limpa a tela do terminal, compatível com Windows e outros sistemas.
- **Variáveis principais**:
  - `saldo`: valor inicial do saldo do usuário.
  - `senha_user`: senha pré-definida para acesso.
- **Fluxo de execução**:
  - Autenticação.
  - Seleção de operação.
  - Processamento do saque e recibo.
  - Mensagens de finalização e saldo final.

## Observações

- Este é um projeto simples, com objetivo educacional.
- Não utiliza métodos de segurança avançados.
- O saldo e senha são definidos diretamente no código.
- Para aprimorar, pode-se implementar mais funcionalidades como depósitos, transferências, múltiplos usuários, entre outros.

## Autor

Desenvolvido por [MarcosPires04](https://github.com/MarcosPires04) para estudos universitários.

---
