# Instalação por plataforma

## ChatGPT

1. Baixe `dist/prontuario-upa-chatgpt.zip`.
2. Se sua conta/ambiente oferecer importação de plugins, importe o ZIP por esse recurso.
3. Ative o Prontuário UPA e solicite uma admissão ou evolução com dados fictícios para conferir o resultado.

A disponibilidade da importação depende do produto e da conta. Anexar o ZIP a uma conversa não instala automaticamente um plugin. Como alternativa manual, use o conteúdo de `gemini/instrucoes.md` nas instruções de um projeto ou assistente personalizado que aceite esse volume de texto, ou como arquivo de referência com uma instrução explícita para seguir o modelo. Isso não equivale à instalação nativa.

## Claude

1. Baixe `dist/prontuario-upa-claude.zip`.
2. Na área de Skills/Habilidades, escolha a opção de enviar uma Skill personalizada, quando disponível.
3. Envie o ZIP e ative a Skill.
4. Solicite: “Faça uma admissão no modelo Prontuário UPA com os dados que vou enviar”.

O ZIP contém `prontuario-upa/SKILL.md`. A disponibilidade de Skills depende do plano e das permissões da organização.

Referência oficial: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## Gemini CLI — habilidade (Agent Skill)

Requer o Gemini CLI instalado, autenticado e com suporte a Agent Skills. A instalação descrita aqui é para o CLI; a interface web de Gems é um produto diferente.

1. Instale a habilidade a partir deste repositório:

   ```sh
   gemini skills install https://github.com/hampikamayuq/prontuario-upa.git --path gemini/prontuario-upa
   ```

2. No Gemini CLI, execute `/skills reload` e `/skills list` e confirme que `prontuario-upa` aparece na lista.
3. Solicite: “Use a habilidade prontuario-upa para fazer uma admissão com os dados fictícios que vou enviar”.
4. Quando o Gemini solicitar autorização para ativar a habilidade, confira os detalhes e confirme.

Para instalar a partir do download, baixe `dist/prontuario-upa-gemini.zip`, extraia-o e execute `gemini skills install ./prontuario-upa` no diretório onde extraiu o ZIP. A pasta contém `SKILL.md` e `LICENSE`.

Referência oficial: https://geminicli.com/docs/cli/skills/

## Verificação antes do uso

As adaptações preservam o conteúdo-base 0.1.4, mas ainda não foram testadas em sessões de Claude e Gemini. Confira o modelo com casos fictícios, inclusive pediatria, dados incompletos e exames alterados. Revise os campos de exame físico preenchidos automaticamente. Nenhuma instalação garante resultados idênticos entre modelos.

## Atualizar e gerar pacotes

Edite `skills/instructions/SKILL.md` como fonte principal e execute `python3 scripts/package.py`. Reimporte os pacotes de ChatGPT e Claude. No Gemini CLI, desinstale a versão anterior com `gemini skills uninstall prontuario-upa`, repita a instalação e execute `/skills reload`. Não publique dados reais de pacientes neste repositório.
