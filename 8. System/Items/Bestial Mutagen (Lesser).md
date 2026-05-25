---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Your features transform into something bestial and lumbering.

**Benefit** You gain a +1 item bonus to Athletics checks and unarmed attack rolls. You gain a claw unarmed attack (1d4 slashing damage) with the agile trait and a jaws unarmed attack (1d6 piercing damage). [[Striking]] runes don't modify the damage caused by these attacks.

**Drawback** You take a -2 penalty to Reflex saves, Acrobatics checks, and Stealth Checks.

**Duration** 1 minute.

> [!danger] Effect: Bestial Mutagen (Lesser)

**Source:** `= this.source` (`= this.source-type`)
