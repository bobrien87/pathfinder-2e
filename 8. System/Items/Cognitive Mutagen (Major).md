---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 3000}"
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

Your mind becomes clear, but physical matters seem ephemeral.

**Benefit** You gain a +4 item bonus to Arcana, Crafting, Lore, Occultism, and Society checks and all checks to [[Recall Knowledge]]. Your critical failures on Recall Knowledge checks become failures instead. You become trained in one skill, chosen at creation.

**Drawback** You take a -2 penalty to weapon and unarmed attack rolls, Athletics checks, and acrobatics checks. You can carry 2 less Bulk than normal before becoming encumbered, and the maximum Bulk you can carry is reduced by 4.

**Duration** 1 hour.

> [!danger] Effect: Cognitive Mutagen (Major)

**Source:** `= this.source` (`= this.source-type`)
