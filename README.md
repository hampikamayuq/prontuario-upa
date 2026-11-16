# Prontuário UPA

Modelos em português para admissão, evolução e discussão clínica, destinados ao apoio ao médico.

## Downloads

Baixe os arquivos da pasta [dist](dist):

| Plataforma | Arquivo | Uso |
| --- | --- | --- |
| ChatGPT | `prontuario-upa-chatgpt.zip` | Importar como plugin somente em ambientes que ofereçam esse recurso. Enviar o ZIP em uma conversa não equivale a instalar. |
| Claude | `prontuario-upa-claude.zip` | Importar como Skill personalizada e ativá-la, se disponível na conta. |
| Gemini CLI | `prontuario-upa-gemini.zip` | Instalar como habilidade (Agent Skill), conforme o guia de instalação. |

Veja [o guia de instalação](docs/INSTALACAO.md).

## Conteúdo e versão

Base: plugin Prontuário UPA 0.1.4. As regras clínicas originais são preservadas; a embalagem muda conforme a plataforma. A compatibilidade estrutural dos pacotes é conferida; o comportamento ainda precisa ser validado em cada modelo.

- Admissão e evolução em maiúsculas, campos iniciados por `#`.
- Preservação dos dados informados e distinção entre hipóteses, planos e atos realizados.
- Conduta numerada, curta e pertinente ao caso.
- Exame físico padrão quando ausente, com observação ao médico fora do registro. É indispensável revisar esses campos antes de copiar para o prontuário.

## Uso responsável

Ferramenta de apoio: toda saída exige revisão do médico assistente. Não é integração com prontuário eletrônico nem serviço de diagnóstico autônomo. Não publique dados identificáveis de pacientes em issues, exemplos ou pull requests.

## Atualizações

Não há atualização automática entre GitHub, ChatGPT, Claude e Gemini. Baixe novamente o pacote ou atualize as instruções quando houver nova versão.

## Autoria e licença

Diego Galvez. Este projeto é distribuído sob a [licença MIT](LICENSE), que permite uso, modificação e redistribuição, inclusive comercial, desde que o aviso de copyright e o texto da licença sejam preservados.
