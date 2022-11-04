import os
from datetime import datetime

class Console:
    def __init__(self):
        pass

    @property
    def time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def toOsColor(self, value: int = 249) -> str:
        return f"\033[38;5;{value}m"

    def doClear(self) -> "Console":
        os.system("cls" if os.name == "nt" else "clear")
        return self

    def write(
        self, label: str, text: str, top_level_color: int = "@gray:"
    ) -> "Console":
        print(
            (
                (
                    f"{top_level_color}[{self.time}] "
                    f"[{label}] "
                    f"{text}{self.toOsColor()}"
                )
            )
            .replace("@red:", self.toOsColor(52))
            .replace("@gray:", self.toOsColor(242))
            .replace("@dark-green:", self.toOsColor(100))
            .replace("@green:", self.toOsColor(78))
            .replace("@yellow:", self.toOsColor(226))
            .replace("@blue:", self.toOsColor(33))
            .replace("@pink:", self.toOsColor(135))
        )
        return self

    def writeDeath(self, text: str, top_level_color: int = "@red:") -> "Console":
        print(
            (f"{top_level_color}{text}{self.toOsColor()}")
            .replace("@red:", self.toOsColor(52))
            .replace("@gray:", self.toOsColor(242))
            .replace("@dark-green:", self.toOsColor(100))
            .replace("@green:", self.toOsColor(78))
            .replace("@yellow:", self.toOsColor(226))
            .replace("@blue:", self.toOsColor(33))
            .replace("@pink:", self.toOsColor(135))
        )
        return self

    def inp(self, text: str, top_level_color: int = "@gray:") -> "Console":
        return input(
            (
                (
                    f"[{self.time}] "
                    f"[Input] "
                    f"{text}{self.toOsColor()}"
                )
            )
            .replace("@red:", self.toOsColor(52))
            .replace("@gray:", self.toOsColor(242))
            .replace("@dark-green:", self.toOsColor(100))
            .replace("@green:", self.toOsColor(78))
            .replace("@yellow:", self.toOsColor(226))
            .replace("@blue:", self.toOsColor(33))
            .replace("@pink:", self.toOsColor(135))
        )


console = Console()
console.doClear()
console.inp("Data Url: ", top_level_color="@pink")