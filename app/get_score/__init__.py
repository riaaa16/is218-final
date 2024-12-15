'''
Validates form inputs
- Used nested dictionary as part of validation
Calculates score after validation
'''
from dataclasses import dataclass
from typing import Union

# Type union for numeric inputs
Number = Union[int, float]

@dataclass
class Score:
    '''
    1. Validates all inputs as vaild numbers
        - num_chars must be an int or float
        - if float, must be equivalent to an int
        - greater than 0
    2. Calculates score after validation check
    '''
    finish: Number
    color: Number
    shading: Number
    bg: Number
    size: Number
    num_chars: Number

    def __repr__(self) -> str:
        '''String representation for debugging and logging'''
        return (
            f"Finish: {scoreMap['finish'][self.finish]} = {self.finish}\n" +
            f"Color: {scoreMap['color'][self.color]} = {self.color}\n" +
            f"Shading: {scoreMap['shading'][self.shading]} = {self.shading}\n" +
            f"Background: {scoreMap['background'][self.bg]} = {self.bg}\n" +
            f"Size: {scoreMap['size'][self.size]} = {self.size}\n" +
            f"Characters: {self.num_chars}\n"
        )

    def __str__(self) -> str:
        '''String representation for users to read'''
        return (
            f"Finish: {scoreMap['finish'][self.finish]}\n" +
            f"Color: {scoreMap['color'][self.color]}\n" +
            f"Shading: {scoreMap['shading'][self.shading]}\n" +
            f"Background: {scoreMap['background'][self.bg]}\n" +
            f"Size: {scoreMap['size'][self.size]}\n" +
            f"Characters: {self.num_chars}\n"
        )

    def calculate(self) -> Number:
        '''
        If all inputs pass validation check,
        calculate and return the score
        '''
        self.validate()
        return (self.finish + self.color + self.shading + self.bg) * self.size * self.num_chars

    def validate(self):
        '''
        Puts params finish - size in a dictionary
        Compares user-inputted values to the key-value pairs
        in nested dictionary scoreMap

        Validates num_chars as a positive whole number
        (or whole number equivalent) 
        '''
        # Put params in dictionary
        keys = {
            "finish": self.finish,
            "color": self.color,
            "shading": self.shading,
            "background": self.bg,
            "size": self.size,
        }

        # Check each key explicitly
        for category, value in keys.items():
            if value not in scoreMap[category]:
                raise KeyError(f"Invalid or missing option for {category}: {value}")

        # Check character count | LYBYL
        if (
            not isinstance(self.num_chars, (int, float))
            or self.num_chars <= 0
            or (self.num_chars % 1 != 0)
        ):
            raise ValueError(
                "Please use whole numbers for the character count. " +
                "The character count must be greater than 0."
                )
        # if Positive Whole Number, convert into an int
        self.num_chars = int(self.num_chars)

scoreMap = {
    # Nested Dictionary with the defined options for each param
    # except numChars
    "finish" : {
        5 : "Rough Sketch",
        10 : "Cleaned | Lined | Lineless"
    },
    "color" : {
        0 : "Uncolored",
        5 : "Rough Color",
        10 : "clean Color | Painted"
    },
    "shading" : {
        0 : "Unshaded",
        5 : "Minimal Shading",
        10 : "Full Shading"
    },
    "background" : {
        0 : "No Background | Minimal | Photo",
        5 : "Pattern | Abstract",
        10 : "Props | Scene Elements | Design Layout",
        20 : "Full Scene"
    },
    "size" : {
        0.5 : "Simple",
        1 : "Portrait | Bust",
        1.5 : "Half-body",
        2 : "Full-body"
    }
}
