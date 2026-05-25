---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Mental]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 2000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you hold this sleek, shiny gray wand, you hear a faint chorus of overlapping whispers.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Mind Probe]]. The first time the target rolls a success at a Deception check to mislead your probe, it gets a result one step worse than it rolled. This means you learn the answer if the target's Deception check would have succeeded, and you learn nothing rather than believing a falsehood if the check would have been a critical success.

**Craft Requirements** Supply a casting of [[Mind Probe]].

**Source:** `= this.source` (`= this.source-type`)
