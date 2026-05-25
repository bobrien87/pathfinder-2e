---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 2}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tripods are designed for use with kickback weapons, as a way for gunslingers with lower strength to accurately use these more powerful weapons by sacrificing mobility instead. They can be set up and attached to a firearm with a single Interact action using one hand, setting the tripod in your square. If the kickback weapon requires two hands, you can change your grip on the weapon as part of this action. While this sturdy piece of engineering is in use, you don't take the -2 penalty for firing a kickback weapon, even if your Strength isn't high enough to avoid the penalty. However, you must retrieve the tripod with a single Interact action before you can move the firearm to a different position. Normally, when you're [[Hidden]] or [[Undetected]], you become observed if you do anything except [[Hide]], [[Sneak]], or Step. However, deploying or retrieving a tripod with an Interact action doesn't automatically make you observed, so long as you don't set up or remove the tripod when it's in a spot where creatures can see the tripod itself.

**Source:** `= this.source` (`= this.source-type`)
