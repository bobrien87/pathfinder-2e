---
type: ancestry
source-type: "{source-type}"
traits: "{traits}"
hp: "{hp}"
size: "{size}"
speed: "{speed}"
boosts: "{boosts}"
flaws: "{flaws}"
languages: "{languages}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

**Base HP** `= this.hp` | **Size** `= this.size` | **Speed** `= this.speed` feet
`= choice(this.boosts != null, "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null, choice(this.boosts != null, "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null, choice(this.boosts != null or this.flaws != null, "<br>", "") + "**Languages** " + this.languages, "")`

***

{description}

#### Heritages
{heritages}

**Source:** `= this.source` (`= this.source-type`)
