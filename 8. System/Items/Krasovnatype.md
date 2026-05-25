---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 15}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A krasovnatype (named after Dr. Krasovna Gerenevich) consists of a carefully prepared silvered glass plate charged by a Stasian coil. When you touch the front of the glass or hold it near a living creature within your reach, an image of that creature's aura is imprinted on the glass. Once a krasovnatype has an image on it, you can't use the glass plate on another creature. If you are trained in Occultism, you can look at the image and learn if the associated creature has innate, prepared, or spontaneous spellcasting, along with the tradition of that casting and the highest rank of spells they can cast. Referencing the image grants a +1 item bonus to any Recall Knowledge check regarding the creature.

**Source:** `= this.source` (`= this.source-type`)
