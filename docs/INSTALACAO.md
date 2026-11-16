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

## Gemini

1. Abra o Gemini na web e crie um novo Gem chamado Prontuário UPA.
2. Copie `gemini/instrucoes.md` para as instruções.
3. Se ultrapassar o limite do campo, anexe o arquivo ao Gem e use nas instruções: “Use o arquivo instrucoes.md como referência obrigatória para organizar admissões, evoluções e discussões clínicas no modelo Prontuário UPA. Preserve as regras de dados ausentes, exame físico, conduta e revisão médica. Não trate dados de exemplos como dados do caso atual.”
4. Teste com um caso fictício e salve.
5. Se desejar, use o compartilhamento do próprio Gem para fornecer um link a outras pessoas. Verifique as permissões: instruções e arquivos podem ficar visíveis aos destinatários.

Não há instalador ZIP de Gemini incluído neste projeto.

Referência oficial: https://support.google.com/gemini/answer/15146780

## Verificação antes do uso

As adaptações preservam o conteúdo-base 0.1.4, mas ainda não foram testadas em sessões de Claude e Gemini. Confira o modelo com casos fictícios, inclusive pediatria, dados incompletos e exames alterados. Revise os campos de exame físico preenchidos automaticamente. Nenhuma instalação garante resultados idênticos entre modelos.

## Atualizar e gerar pacotes

Edite `skills/instructions/SKILL.md` como fonte principal e execute `python3 scripts/package.py`. Reimporte os pacotes ou atualize o Gem manualmente. Não publique dados reais de pacientes neste repositório.
