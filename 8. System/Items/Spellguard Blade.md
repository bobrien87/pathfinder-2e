---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Agile]]", "[[Disarm]]", "[[Finesse]]", "[[Magical]]", "[[Parry]]", "[[Versatile s]]"]
price: "{'gp': 320}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The guard of this *+1 striking main-gauche* is inscribed with eldritch glyphs that guard against magic.

When you are benefiting from the +1 circumstance bonus to AC from this weapon's parry trait, you also apply that circumstance bonus to your saving throws against spells that target you.

> [!danger] Effect: Spellguard Blade

**Source:** `= this.source` (`= this.source-type`)
