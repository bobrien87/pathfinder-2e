---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Poison]]", "[[Wand]]"]
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

This wand is made of chitin, topped with a hooked barb that weeps droplets of foul-smelling, green fluid when you Activate the wand.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast a 6th-rank [[Spider Sting]], but it deals 3d6 untyped damage on a touch or on a successful save, and delivers this poison.

**Deadly Spider Venom** (poison, virulent) **Level** 11

**Maximum Duration** 6 rounds

**Stage 1** 3d6 poison damage and [[Enfeebled]] 2 (1 round)

**Stage 2** 4d6 poison damage and enfeebled 2 (1 round)

**Stage 3** 6d6 poison damage and enfeebled 2 (1 round)

**Craft Requirements** Supply a casting of *spider sting* at 6th-rank.

**Source:** `= this.source` (`= this.source-type`)
