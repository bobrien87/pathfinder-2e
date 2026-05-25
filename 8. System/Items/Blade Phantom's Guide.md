---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 300, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A blade phantom's guide is a metal rectangle, often on a chain, etched with an image of a warrior in a fighting stance. When you apply a *blade phantom's guide* to a weapon, it summons a spiritual fragment of a warrior who was adept with that weapon. For 1 minute, you treat your proficiency with that weapon as equal to your highest weapon proficiency. This effect cannot affect a weapon whose level is higher than the *blade phantom's guide* (11th).

**Source:** `= this.source` (`= this.source-type`)
