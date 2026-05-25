---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

Even in death, a dragon's gaze is terrible to behold. When used to cast [[Breathe Fire]] at 3rd rank or higher, an eye from a dragon causes the spell to manifest some of the creature's fearsome aura and inspire terror. Creatures in the spell's area must attempt a basic Will save instead of a basic Reflex save, and in addition to taking the spell's normal damage on a failure, they're [[Frightened]] 1. This adds the emotion, fear, and mental traits to the spell.

> [!danger] Effect: Dragon Eye

**Source:** `= this.source` (`= this.source-type`)
