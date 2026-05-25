---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 18}"
usage: "held-in-one-plus-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This complex wooden device, worn on the back, contains a miniature ballista on a retractable arm. As an Interact action, you can pull a lever to deploy or retract the ballista. As long as it remains deployed, you must hold the ballista using that hand or some of the components spill out onto the ground, just like dropping any other weapon. While deployed, the device opens and raises the ballista up over your shoulder. While retracted, the ballista and its mount slide down and are concealed within the device. Although a backpack ballista packs a punch, the device is a challenge to operate. Reloading it takes 1 minute and can't be done while worn. As normal, you can't wear a backpack ballista with another backpack.

**Source:** `= this.source` (`= this.source-type`)
