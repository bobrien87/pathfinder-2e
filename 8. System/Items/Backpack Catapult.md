---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Volley 50]]"]
price: "{'gp': 20}"
usage: "held-in-one-plus-hands"
bulk: "3"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden device is worn on the back and contains a miniature catapult mounted on a retractable frame. As an Interact action, you can pull a lever to deploy or retract the catapult. As long as it remains deployed, you must hold the catapult using that hand or some of the components spill out onto the ground, just like dropping any other weapon. While deployed, the device opens and raises the catapult up over your shoulder. While retracted, the catapult and its mount slide down and are [[Concealed]] within the device. A backpack catapult fires specialized stone spheres that are loaded into the bucket while unworn and retracted, through a sliding hatch; the reloading process takes 1 minute. To prevent misfires and accidental injury, the bucket fully encloses the stone while deployed, only opening when fired. As normal, you can't wear a backpack catapult with another backpack.

**Source:** `= this.source` (`= this.source-type`)
