---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Visual]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 250, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Thin, shiny wires crisscross the surface of this smooth, black wand. The pommel is capped with a polished metal sphere, which sometimes emits small electric sparks.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Blur]], and the wand creates faint orbs of electricity [[Concealed]] in the haze around you. Each time a creature that's adjacent to you fails a flat check against the concealment from blur, they explode one of the orbs, causing them to take 5 electricity damage.

**Craft Requirements** Supply a casting of *blur*.

**Source:** `= this.source` (`= this.source-type`)
