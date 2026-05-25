---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Arcane]]", "[[Invested]]"]
price: "{'gp': 650}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hat comes in many forms, such as a colorful turban or a pointy hat with a brim, and is adorned with symbols or runes. It grants you a +2 item bonus to Arcana checks and allows you to cast the  cantrip as an arcane innate cantrip.

This larger, fancier hat can be activated. Each *greater mage's hat* has a specific 4th-rank summon spell from the arcane list woven into its fabric, typically [[Summon Animal]] or [[Summon Elemental]]. If you prepare arcane spells, you can change the spell to a different 4th-rank arcane summon spell you know when you invest it.

**Activate—Hat Spell** Cast a Spell

**Frequency** once per day

**Effect** You doff the hat, causing magical energy to pour from it. You cast the spell stored in the hat.

**Source:** `= this.source` (`= this.source-type`)
