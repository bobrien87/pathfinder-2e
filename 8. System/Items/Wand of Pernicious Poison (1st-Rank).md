---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Poison]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 100, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand is made of chitin, topped with a hooked barb that weeps droplets of foul-smelling, green fluid when you Activate the wand.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Spider Sting]], but it gains the virulent trait.

**Craft Requirements** Supply a casting of *spider sting.*

**Source:** `= this.source` (`= this.source-type`)
