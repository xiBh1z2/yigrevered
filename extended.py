from discord.ext import commands as cmd


class Context(cmd.Context):
    def __init__(self, **attrs):
        super().__init__(**attrs)

    @property
    def log(self):
        return self.bot.log

    @property
    def db(self):
        return self.bot.db

    @property
    def em(self):
        return self.bot.em

    @property
    def config(self):
        return self.bot.config
