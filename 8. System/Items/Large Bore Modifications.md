---
type: item
source-type: "Remaster"
level: "5"
price: "{'gp': 120}"
usage: "attached-to-firearm"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These modifications include a heavier stock and larger replacement barrel designed to increase the stopping power of firearms. *Large bore modifications* can only be applied to firearms with the kickback or scatter traits, and attaching *large bore modifications* takes 1 hour, though this time can overlap with the standard time required to maintain and clean your firearm to prevent misfires.

When you attach *large bore modifications* to a kickback weapon, the bonus to damage granted by the kickback trait increases from 1 to 2 additional Damage and the Strength requirement to fire the weapon without penalty increases to +4.

When you attach *large bore modifications* to a weapon with the scatter trait, the radius of the scatter effect increases by 5 feet, but the weapon imposes a -2 penalty on attack rolls if the wielder's Strength modifier is less than +2. If the weapon has both the kickback and scatter traits, apply both sets of modifications with the Strength requirement raised to +4 to avoid penalties when firing.

**Source:** `= this.source` (`= this.source-type`)
