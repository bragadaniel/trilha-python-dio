# Documentação — Fundamentos (Banco Simples)

## Objetivo

- Reorganizar e modularizar a implementação atual separando responsabilidades.
- Adicionar funções para cadastro de usuário e criação de conta.

## Visão geral das tarefas

- Extrair/transformar as operações existentes em funções pequenas e testáveis:
    - Saque
    - Depósito
    - Visualizar extrato
- Implementar gerenciamento de usuários
- Implementar gerenciamento de contas (vinculadas a usuários)

## Assinaturas e regras das funções

- Saque
    - Deve ser keyword-only (usar `*` na assinatura).
    - Argumentos esperados: `saldo`, `valor`, `extrato`, `limite`, `numero_saques`, `limite_saques`.
    - Retorno: tupla `(novo_saldo, extrato)`.
    - Regras típicas: não permitir saque se `valor > limite` ou se `numero_saques >= limite_saques`.

- Depósito
    - Deve ser positional-only (usar `/` na assinatura).
    - Argumentos esperados: `saldo`, `valor`, `extrato`.
    - Retorno: tupla `(novo_saldo, extrato)`.

- Extrato
    - Deve aceitar `saldo` como positional e `extrato` como keyword-only.
    - Assinatura recomendada: `def extrato(saldo, *, extrato):`.

Exemplos de assinaturas (Python):

```py
def sacar(*, saldo: float, valor: float, extrato: list, limite: float, numero_saques: int, limite_saques: int) -> tuple:
        ...

def depositar(saldo, valor, extrato, /) -> tuple:
        ...

def extrato(saldo, *, extrato):
        ...
```

## Estruturas de dados — Usuários

- Armazenar usuários em uma lista (por exemplo: `usuarios = []`).
- Cada usuário deve conter os campos:
    - `nome` (string)
    - `data_nascimento` (string, formato livre ou ISO)
    - `cpf` (string ou número) — deve ser único
    - `endereco` (string) — formato sugerido: "logradouro, número - bairro - cidade/UF"

Validações mínimas:
- Verificar CPF único antes de cadastrar.

## Estruturas de dados — Contas

- Armazenar contas em uma lista (por exemplo: `contas = []`).
- Cada conta deve conter:
    - `agencia` (string) — padrão: `'0001'`
    - `numero` (int) — sequencial e único por conta
    - `usuario_cpf` (referência ao CPF do usuário)

Regras:
- Uma conta se vincula a um usuário (1 usuário pode ter N contas).
- Geração de `numero` pode ser feita com um contador sequencial.

## Fluxo sugerido de operações

1. Cadastrar usuário (verificar CPF único)
2. Criar conta vinculada ao CPF do usuário
3. Utilizar `depositar` e `sacar` para atualizar saldo e `extrato`
4. Consultar `extrato(saldo, extrato=extrato)` para mostrar histórico

## Exemplo mínimo de uso

```py
usuarios = []
contas = []
extrato = []
saldo = 0.0

# cadastrar usuário
# criar conta
# depositar/ sacar
# imprimir extrato
```

## Dicas de implementação

- Mantenha cada função pequena e com responsabilidade única.
- Use mensagens de erro claras para validar condições de negócio (ex.: saldo insuficiente, limite diário atingido, CPF já cadastrado).
- Separe a lógica de entrada/saída (IO) da lógica de negócio para facilitar testes.

## Próximos passos

- Implementar as funções com base nas assinaturas sugeridas.
- Adicionar testes unitários simples para cada função.
- Integrar ao `desafio.py` mantendo a interface de usuário (input/print) no nível superior.

