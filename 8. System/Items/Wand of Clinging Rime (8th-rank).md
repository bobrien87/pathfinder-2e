---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Cold]]", "[[Magical]]", "[[Wand]]", "[[Water]]"]
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

A thin layer of frost coats this gnarled holly wand.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 8th-rank [[Frigid Flurry]]. After you cast the spell, the ice crystals freeze to flesh and other surfaces, clinging to the creatures in the area. Each creature that fails its save takes 2d6 persistent,cold damage.

**Craft Requirements** Supply a casting of [[Frigid Flurry]] of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
