---
type: item
source-type: "Remaster"
level: "4"
price: "{'gp': 75}"
usage: "attached-to-crossbow-or-firearm-firing-mechanism"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Air cartridge firing mechanisms use a container of compressed air affixed to a sealed system that releases the air in a small burst to propel ammunition, and they're the default used in Arcadian air repeaters. Any firearm can be modified to replace its normal firing mechanism with an air cartridge firing system, allowing the weapon to be fired underwater or in other conditions that would normally prevent the ignition of black powder. The air cartridges lack much of the propulsive power of black powder, however, imposing a –10-foot penalty to the attached firearm's range increment. Weapons with the kickback trait don't gain that trait's benefits when using an air cartridge firing system. Attaching an air cartridge firing system takes one hour, though this time can overlap with the standard time required to maintain and clean your firearm to prevent misfires.

**Source:** `= this.source` (`= this.source-type`)
