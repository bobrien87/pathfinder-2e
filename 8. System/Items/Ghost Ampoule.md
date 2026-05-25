---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Auditory]]", "[[Consumable]]", "[[Emotion]]", "[[Expandable]]", "[[Fear]]", "[[Mental]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A daub of ectoplasm twitches within this glass container, faintly glowing with ghostly light. When opened, it forms the echo of a departed spirit, which looks like a Medium ghost. You can throw the ampoule up to 30 feet when you Activate it. The ghost utters a final lament, forcing each living creature in a @Template[emanation|distance:15] except you to attempt a DC 18 [[Will]] save. On a failure, a creature becomes [[Frightened]] 2 (or [[Frightened]] 3 on a critical failure).

**Craft Requirements** Supply ectoplasmic residue from a destroyed ghost.

**Source:** `= this.source` (`= this.source-type`)
