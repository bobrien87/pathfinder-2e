---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 12}"
usage: "affixed-to-a-ranged-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A demolition fulu allows a saboteur or excavator to be far away from the scene when demolition happens. The fulu crumbles to ash over 5 minutes to 8 hours, as you determine when you place the fulu. Once the duration ends, the fulu lowers the Hardness of the object it's affixed to by an amount equal to the fulu's level and then deals 3d6 bludgeoning to the object. A demolition fulu serves as a hazard with a DC 17 [[Perception]] check to detect it and DC 17 [[Thievery]] check to disable it according to its type.

**Source:** `= this.source` (`= this.source-type`)
