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

Your features become striking, and your voice becomes musical and commanding, though emotion clouds your reason.

**Benefit** You gain a +4 item bonus to Deception, Diplomacy, Intimidation and Performance checks. Your critical failures with any of these skills become failures instead.

**Drawback** You take a -2 item penalty to Arcana, Crafting, Lore, Occultism, and Society checks. Choose one skill in which you are trained; for the duration, you become untrained in that skill. All your failures to [[Recall Knowledge]] become critical failures.

**Duration** 1 hour.

> [!danger] Effect: Silvertongue Mutagen (Major)

**Source:** `= this.source` (`= this.source-type`)
