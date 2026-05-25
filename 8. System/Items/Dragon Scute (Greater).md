---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 14000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

The thick plates that form the strongest points in a dragon's armor can be used as powerful defensive catalysts. Using one of these scales to cast [[Mountain Resilience]] causes the target's skin to grow a thick layer of draconic scales. Instead of the spell's normal effects, the target gains damage resistance based on the type and dragon's tradition.

The scale can be used with *mountain resilience* of 10th rank or higher.

**Arcane** resistance 10 against all damage from spells

**Divine** resistance 20 to spirit, vitality, and void

**Occult** resistance 20 to mental

**Primal** resistance 15 to bludgeoning, piercing, slashing, and poison

**Source:** `= this.source` (`= this.source-type`)
