---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Detection]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 6}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to armor

**Activate** `pf2:f` (concentrate)

**Trigger** A [[Hidden]] or [[Undetected]] enemy hits you with an attack

**Requirements** You are trained in Survival

This talisman is a ring of dried, interwoven pieces of straw. When you activate the *hunter's bane*, you sense the exact location of the attacker. It becomes [[Observed]] by you if it was hidden from you or becomes hidden from you if it was undetected. If the attacker is behind lead, the *hunter's bane* has no effect.

**Source:** `= this.source` (`= this.source-type`)
