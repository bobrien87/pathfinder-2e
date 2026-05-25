---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Wand]]", "[[Water]]"]
price: "{'cp': 0, 'gp': 1000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This blackened wood wand has a smoldering tip, emitting a slight trail of steam.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Cinder Swarm]], but the mist prevents creatures from being able to breathe in its area. They must hold their breath or start suffocating.

> [!danger] Effect: Remaining Air

**Craft Requirements** Supply a casting of [[Cinder Swarm]].

**Source:** `= this.source` (`= this.source-type`)
