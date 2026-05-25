---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Capacity 4]]", "[[Cobbled]]", "[[Concussive]]", "[[Fatal d8]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This dubious weapon gets its name from the fact that it's typically crafted with multiple false barrels so that it's more difficult for enemies to predict the weapon's angle of fire from the four working barrels. Most of the time, this gun functions as a *+1 striking pepperbox* with capacity 4 instead of capacity 3, albeit one with a complicated loading mechanism involving rotating the barrels. In a pinch though, all four of the real barrels can be fired simultaneously.

**Activate—Everywhere Shot** `pf2:2` Interact

**Effect** Make up to four Strikes with the liar's gun. Each of the four Strikes must be against a different target within a @Template[type:cone|distance:20]. You apply and increase your multiple attack penalty for the four Strikes only after resolving all attacks. If the weapon misfires on any of these attacks, wait to apply the misfire until you resolve all of the attacks.

**Source:** `= this.source` (`= this.source-type`)
