---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Cobbled]]", "[[Goblin]]", "[[Modular]]", "[[Scatter 5]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

No one's entirely certain who developed the spoon gun, but all authorities agree that it was probably a goblin. Essentially a terrible idea in firearm form, the spoon gun is a spring-powered hand cannon with a modified grip that uses miscellaneous knives, forks, chopsticks, and spoons as ammunition. Users typically upend the entire contents of their cutlery drawer into the gun, aim it in the general direction of the foe, and hope it hits something.

This hand cannon is a martial weapon, instead of a simple weapon. It has the scatter (5 feet) trait and uses cutlery or similar-sized objects as ammunition instead of bullets (enough cheap cutlery to fire ten shots costs 1 sp).

**Source:** `= this.source` (`= this.source-type`)
