---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Acid]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 4500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This greasy stick emits a stomach-churning scent when held in a hand.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Acid Grip]] at 6th rank. A creature that takes initial acid damage from this spell become [[Sickened]] 1. Use your spell DC if the creature attempts to recover from this sickness. This is an olfactory effect.

**Craft Requirements** Supply a casting of *acid grip* at 6th rank

**Source:** `= this.source` (`= this.source-type`)
