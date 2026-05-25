---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Electricity]]", "[[Magical]]", "[[Mental]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A two-pronged metal rod, this wand has a handle coated in thick rubber. Each prong ends in a copper coil. When Activated, the wand produces a loud zapping sound.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Paralyze]], electrocuting the target into immobility. Each target takes 1d12 electricity damage at the start of its turns while it remains stunned or [[Paralyzed]] due to the spell.

**Craft Requirements** Supply a casting of *paralyze* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
