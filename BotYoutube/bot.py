"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    # Abre o canal da Python Brasil no YouTube
    bot.browse("https://www.youtube.com/@pythonbrasiloficial")

    # Implement here your logic...
    if not bot.find("sobre", matching=0.97, waiting_time=10000):
        bot.not_found("sobre")
    bot.click()

    # Procurando pela âncora referente ao número de inscritos
    if not bot.find("inscritos", matching=0.97, waiting_time=10000):
        not_found("inscritos")
    bot.click_relative(-4, 10)

    # Selecionando o valor da página
    bot.mouse_down()
    bot.move_relative(-50, 0)
    bot.mouse_up()

    # Coletando o valor do clipboard
    bot.control_c()
    numero_inscritos = bot.get_clipboard()
    print(f"Inscritos => {numero_inscritos}")

    # Procurando pela âncora referente ao número de visualizações
    if not bot.find("visualizacoes", matching=0.97, waiting_time=10000):
        not_found("visualizacoes")
    bot.click_relative(-3, 9)

    # Selecionando o valor da página
    bot.mouse_down()
    bot.move_relative(-50, 0)
    bot.mouse_up()

    # Coletando o valor do clipboard
    bot.control_c()
    numero_visualizacoes = bot.get_clipboard()
    print(f"Número de visualizações => {numero_visualizacoes}")

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Tarefa BotYoutube finalizada com sucesso"
    )

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()