---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Scatter 5]]"]
price: "{'gp': 7}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Similar to the blunderbuss, a dragon-mouth pistol fires pellets from a flared barrel. Though less powerful than a blunderbuss, the dragon-mouth pistol is appreciated for its portability and one-handed design. Though the name was coined because of the destructive belch of this handheld scatter weapon, many gunsmiths craft dragon-mouth pistols with elaborate embellishments that resemble a stylized dragon's maw framing the barrel.

**Source:** `= this.source` (`= this.source-type`)
