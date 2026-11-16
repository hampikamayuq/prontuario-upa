# Prontuário UPA

Modelos em português para admissão, evolução e discussão clínica, destinados ao apoio ao médico.

## Downloads

Use os arquivos indicados abaixo; os pacotes ZIP estão na pasta [dist](dist):

| Plataforma | Arquivo | Uso |
| --- | --- | --- |
| ChatGPT | [prontuario-upa-chatgpt.zip](dist/prontuario-upa-chatgpt.zip) | Importar como plugin somente em ambientes que ofereçam esse recurso. Enviar o ZIP em uma conversa não equivale a instalar. |
| Claude | [prontuario-upa-claude.zip](dist/prontuario-upa-claude.zip) | Importar como Skill personalizada e ativá-la, se disponível na conta. |
| Gemini (aplicativo) | [instrucoes.txt](gemini/instrucoes.txt) ou [instrucoes.md](gemini/instrucoes.md) | Em Habilidades → +, use Criar com o Gemini e anexe o arquivo, ou Criar manualmente e cole as instruções. |
| Gemini CLI (opcional) | [prontuario-upa-gemini.zip](dist/prontuario-upa-gemini.zip) | Instalar como habilidade (Agent Skill), conforme o guia de instalação. |

Veja [o guia de instalação](docs/INSTALACAO.md) para os passos completos de cada plataforma.

## Instalação no aplicativo Gemini

Baixe [instrucoes.txt](gemini/instrucoes.txt), que pode ser aberto em leitores de texto comuns. A [versão .md](gemini/instrucoes.md) tem exatamente o mesmo conteúdo. Na página do arquivo no GitHub, use a opção de baixar o arquivo bruto.

Escolha uma das duas formas de criar a habilidade:

- **Criar com o Gemini:** abra **Habilidades → + → Criar com o Gemini**, anexe `instrucoes.txt` e peça: “Crie uma habilidade chamada prontuario-upa usando o arquivo anexado. Preserve integralmente as regras clínicas, a estrutura dos registros e as orientações de revisão médica, sem resumir nem omitir regras”. Revise as instruções propostas e conclua a criação.
- **Criar manualmente:** abra **Habilidades → + → Criar manualmente**, use o nome `prontuario-upa` e cole todo o conteúdo de `instrucoes.txt` na área de instruções. Conclua a criação.

Confira se `prontuario-upa` aparece em **Instaladas** e teste com um caso fictício. Se já estiver instalada, procure a opção de edição no menu **…** para atualizar as instruções. A disponibilidade de Habilidades depende da conta e da versão do aplicativo.

O ZIP do Gemini CLI é destinado à instalação pelo terminal. Para o aplicativo, use o arquivo `.txt` ou `.md` pelos passos acima.

## Conteúdo e versão

Base: plugin Prontuário UPA 0.1.4. As regras clínicas originais são preservadas; a embalagem muda conforme a plataforma. A compatibilidade estrutural dos pacotes é conferida; o comportamento ainda precisa ser validado em cada modelo.

- Admissão e evolução em maiúsculas, campos iniciados por `#`.
- Preservação dos dados informados e distinção entre hipóteses, planos e atos realizados.
- Conduta numerada, curta e pertinente ao caso.
- Exame físico padrão quando ausente, com observação ao médico fora do registro. É indispensável revisar esses campos antes de copiar para o prontuário.

## Uso responsável

Ferramenta de apoio: toda saída exige revisão do médico assistente. Não é integração com prontuário eletrônico nem serviço de diagnóstico autônomo. Não publique dados identificáveis de pacientes em issues, exemplos ou pull requests.

## Atualizações

Não há atualização automática entre GitHub, ChatGPT, Claude e Gemini. Baixe novamente o pacote ou atualize as instruções quando houver nova versão. No aplicativo Gemini, substitua o texto da habilidade pelo conteúdo atualizado de `instrucoes.txt`.

Para gerar os arquivos a partir da fonte principal `skills/instructions/SKILL.md`, execute `python3 scripts/package.py`. O script atualiza as versões `.txt` e `.md`, as Skills e os pacotes ZIP, incluindo a licença MIT nos pacotes.

## Autoria e licença

Diego Galvez. Este projeto é distribuído sob a [licença MIT](LICENSE), que permite uso, modificação e redistribuição, inclusive comercial, desde que o aviso de copyright e o texto da licença sejam preservados.
