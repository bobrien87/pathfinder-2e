---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 101, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Carved of ash wood and decorated with images of clouds and gusting winds, a *windstep sheath* is a small icon shaped like a weapon sheath or quiver. This whetstone is favored by duelists who like to take their foe by surprise. When you use the [[Quick Draw]] feat with a weapon under the effect of a *windstep sheath*, you can also Step as part of that action, either immediately before or after your Strike.

**Source:** `= this.source` (`= this.source-type`)
