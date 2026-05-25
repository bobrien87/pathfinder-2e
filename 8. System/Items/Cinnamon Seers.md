---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 14}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Zippy, alchemically treated cinnamon suffuses cinnamon seers, a rock candy with a lively taste that provides a mental boost. A cinnamon seer remains in your mouth for 1 hour, its stimulating flavor granting you a +1 item bonus to checks to Recall Knowledge.

> [!danger] Effect: Cinnamon Seers

**Secondary Effect** `pf2:r` (fortune)

**Trigger** You gain no information from a Recall Knowledge check

**Effect** Reroll the triggering check. If this was a secret check, the GM rerolls rather than you; the candy doesn't give you any insight into what the GM rolled, so in that case, you're rerolling based only on guesswork. The seer becomes inert. You become temporarily immune to cinnamon seers until the next time you make your daily preparations.

**Source:** `= this.source` (`= this.source-type`)
