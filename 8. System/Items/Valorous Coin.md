---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 90, 'pp': 0, 'sp': 0}"
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

Valorous coins are metal disks emblazoned with two crossed swords, with inscriptions exhorting bravery and optimism. The effects of a valorous coin last for 1 hour. During that time, if you're reduced below a quarter of your Hit Points while wielding the affected weapon, it empowers you with determination and resolve to finish the fight. You gain temporary Hit Points equal to your level that last for 1 minute, and you gain a +1 circumstance bonus to Strikes and damage rolls with the affected weapon for 1 minute.

> [!danger] Effect: Valorous Coin

Once this minute ends, so do all effects and the remaining duration of the valorous coin, and you're [[Fatigued]] until you're healed to your maximum Hit Points.

**Source:** `= this.source` (`= this.source-type`)
