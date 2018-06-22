# DARK_COMM  Only keep concrete Item classes in this scope!
from .nis import (
    MathematicsNISItem,
    KazakhLanguageNISItem,
    RussianLanguageNISItem,
    EnglishLanguageNISItem,
    QuantitativeNISItem,
)
from .credit import CreditItem
from .unt.compulsory import (
    MathematicalLiteracyCompulsoryUNTItem,
    ReadingLiteracyCompulsoryUNTItem,
    HistoryOfKazakhstanCompulsoryUNTItem,
)
from .unt.profile import (
    MathematicsProfileUNTItem,
    PhysicsProfileUNTItem,
    ChemistryProfileUNTItem,
    BiologyProfileUNTItem,
    GeographyProfileUNTItem,
    HistoryProfileUNTItem,
    EnglishLanguageProfileUNTItem,
    FrenchLanguageProfileUNTItem,
    GermanLanguageProfileUNTItem,
    KazakhLanguageAndLiteratureProfileUNTItem,
    RussianLanguageAndLiteratureProfileUNTItem,
    HumanSocietyRightProfileUNTItem,
)

TEST_SECTION_MAP = {
    "9547": MathematicalLiteracyCompulsoryUNTItem,
    "9546": ReadingLiteracyCompulsoryUNTItem,
    "9545": HistoryOfKazakhstanCompulsoryUNTItem,

    "9548": MathematicsProfileUNTItem,
    "9549": PhysicsProfileUNTItem,
    "9550": ChemistryProfileUNTItem,
    "9551": BiologyProfileUNTItem,
    "9552": GeographyProfileUNTItem,
    "9553": HistoryProfileUNTItem,
    "9554": EnglishLanguageProfileUNTItem,
    "9555": FrenchLanguageProfileUNTItem,
    "9556": GermanLanguageProfileUNTItem,
    "9557": KazakhLanguageAndLiteratureProfileUNTItem,
    "9558": RussianLanguageAndLiteratureProfileUNTItem,
    "9559": HumanSocietyRightProfileUNTItem,
}
