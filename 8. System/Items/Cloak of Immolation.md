---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Appearing as a magic cloak such as a *clandestine cloak*, this garment is made of highly volatile fabric. While wearing it, if you take fire damage, you also take 1d10 persistent,fire damage. Taking fire damage while the persistent fire damage is in effect has no additional effect. You can extinguish the persistent fire damage as normal.

Any creature that hits you with a melee unarmed attack while you are taking this persistent fire damage takes fire damage equal to the persistent fire damage you took on your previous turn. Once the curse has activated for the first time, the cloak fuses to you.

**Source:** `= this.source` (`= this.source-type`)
