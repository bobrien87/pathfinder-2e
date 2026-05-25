---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 80, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you move this delicately carved poplar wand, it looks indistinct, leaving a trail of afterimages in its wake.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Fleet Step]]. For the duration of the spell, you're also [[Concealed]] while you Stride.

**Craft Requirements** Supply a casting of *fleet step*.

**Source:** `= this.source` (`= this.source-type`)
