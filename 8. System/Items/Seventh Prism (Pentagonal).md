---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 52}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

Beloved by the church of the Seventh Veil, a *seventh prism* is a crystal that disperses its internal light, casting an aurora of color. If you use a seventh prism to cast [[Dizzying Colors]], targets are [[Dazzled]] for twice as long as their saving throw indicates. On a critical failure, the target is dazzled for 1 minute after its [[Blinded]] condition ends. Motes of shifting rainbow hues cloud the eyes, making it difficult to see details.

The area increases to a @Template[cone|distance:20], and the DC for the flat check against the target being [[Concealed]] increases to DC 7 flat check.

> [!danger] Effect: Seventh Prism (Pentagonal)

**Source:** `= this.source` (`= this.source-type`)
