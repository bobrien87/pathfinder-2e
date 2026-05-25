---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
bulk: "3"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 half plate* is imbued with a series of runes designed to amplify your voice on the battlefield. You are more readily able to command and motivate the troops, even over the din of battle.

**Activate—Motivate** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** For 1 minute, the volume of your voice is temporarily enhanced, and you gain a +1 status bonus to Diplomacy and Intimidation checks.

> [!danger] Effect: Command Cuirass

**Source:** `= this.source` (`= this.source-type`)
