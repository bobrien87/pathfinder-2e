---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Electricity]]", "[[Gadget]]", "[[Teleportation]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This odd metal rod is often misinterpreted as a mechanical wand of some kind. Any gadgeteer or mage will be able to elaborate on the fact that magic wands do not need to be throughly covered in a copper wire coil and that the pointed quartz crystal at its tip thrums with electricity, not magic.

When activated, electricity courses through you, allowing you to move through the voltage that arcs through the air. You instantly transport yourself and any items you're wearing and holding from your current space to an unoccupied space up to 40 feet away that you can see. If this would bring another creature with you—even if you're carrying it in an extradimensional container—the teleportation fails. You and all creatures in a line between your original location and your destination take @Damage[4[electricity]|options:area-damage] damage.

**Source:** `= this.source` (`= this.source-type`)
