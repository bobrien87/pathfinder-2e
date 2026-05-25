---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 160, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Cracks and healed fractures spiderweb the shaft of this bone wand, worsening each time the wand is used. The bone's worn epiphysis forms the wand's pommel, and black leather wraps around the handle.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Enfeeble]]. After you cast the spell, if the target is [[Enfeebled]], it releases a @Template[emanation|distance:10] that doesn't include itself. Each creature in that area must attempt a Fortitude save as if struck by the *enfeeble* but gets an outcome one degree of success better than it rolled.

**Craft Requirements** Supply a casting of [[Enfeeble]].

**Source:** `= this.source` (`= this.source-type`)
