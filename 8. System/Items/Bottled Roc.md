---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 140}"
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

This bottle contains a shrunken bird preserved with its feathers intact. When opened, the contents reconstitute into a Gargantuan effigy of a great roc, which can appear in the air instead of on the ground. The roc clutches up to two creatures, who become [[Grabbed]], then Flies up to 90 feet and Releases the creatures. The targets must be within 15 feet of the roc; if any of them are unwilling to be grabbed, the roc must [[Grapple]] them with a +17 Athletics modifier or fail to pick them up.

**Craft Requirements** Supply the corpse of a roc.

**Source:** `= this.source` (`= this.source-type`)
