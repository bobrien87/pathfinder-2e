---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Mental]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 24000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This colorfully painted wand has a few jingling bells tied to the pommel.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Uncontrollable Dance]]. When the spell's duration ends, if the target was forced to dance for 1 minute, it becomes [[Fatigued]].

**Craft Requirements** Supply a casting of *uncontrollable dance*.

**Source:** `= this.source` (`= this.source-type`)
