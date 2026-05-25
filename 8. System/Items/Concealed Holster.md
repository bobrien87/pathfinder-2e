---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather holster is crafted to better hide small firearms from view. Only firearms designed for use in one hand are small enough to disguise with this holster. You gain a +1 item bonus to Stealth checks and DCs to hide or conceal a firearm or hand crossbow in this holster.

**Source:** `= this.source` (`= this.source-type`)
