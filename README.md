# Cifra de César

A **Cifra de César**, também conhecida como cifra de troca ou código de César, é uma das técnicas mais simples e conhecidas de criptografia. Este projeto implementa a Cifra de César em Python, permitindo ao usuário codificar ou decodificar mensagens de texto com base em um número fixo de deslocamento.

## Funcionamento
Na Cifra de César, cada letra do texto é substituída por outra que está um número fixo de posições à frente no alfabeto. Por exemplo, com um deslocamento de 3:
- A se torna D
- B se torna E
- C se torna F

O processo é reversível: ao aplicar o deslocamento inverso, é possível decodificar a mensagem.

## Recursos do Código
- **Entrada do Usuário**:
  - Escolha entre codificar (`encode`) ou decodificar (`decode`).
  - Insira a mensagem que deseja processar.
  - Informe o número de deslocamento desejado.
- **Caracteres Suportados**:
  - Letras do alfabeto (a-z).
  - Espaços são mantidos no texto processado.
  - Caracteres especiais e números permanecem inalterados.
- **Execução Contínua**:
  - Após processar uma mensagem, o programa pergunta se o usuário deseja continuar.

## Exemplo de Uso
1. Execute o programa.
2. Escolha `encode` para criptografar ou `decode` para descriptografar.
3. Insira a mensagem e o número de deslocamento.

### Exemplo
Entrada:
Texto: "hello world"
Shift: 5
Modo: "encode"
Saida:
Here is the encoded result: mjqqt btwqi

## Como Executar
1. Certifique-se de ter o Python instalado na sua máquina.
2. Salve o código em um arquivo, como `caesar_cipher.py`.
3. Execute o programa no terminal:
   ```bash
   python caesar_cipher.py
