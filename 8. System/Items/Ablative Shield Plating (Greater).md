---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 70}"
usage: "affixed-to-a-shield"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Ablative shield plating is an amalgam device that provides a layer of additional protection for a shield. Ablative shield plating is cobbled together from parts of other shields, wires, scraps, and bits of detritus, adding mass to a shield. The process of attaching ablative shield plating takes 10 minutes, and you can't attach ablative shield plating to a shield that has any other attached item, such as a shield boss or shield spikes. When the shield is damaged, this additional material crumples, breaks, and falls apart, absorbing some of the energy of the blow. Otherwise, the additional material slowly crumbles over time. Applying the plating grants the shield 20 temporary Hit Points that last for 1 hour or until lost. Removing the plating early destroys it.

**Source:** `= this.source` (`= this.source-type`)
