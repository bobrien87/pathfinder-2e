---
type: item
source-type: "Remaster"
level: "1"
price: "{'sp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Powerful firearms like the arquebus were originally used to defend fortifications or ships, mounted on casements or pintles to steady their aim and offset their recoil. More mobile means of stabilizing weapons with kickback were developed as firearms began to spread across the Inner Sea. The standard tripod takes an Interact action to deploy using one hand.

Monopods are lighter and can be deployed with a single hand using the same action as drawing the firearm. They still require an Interact action to retrieve. Monopods are less stable than a tripod, and firing a kickback weapon from a monopod without the necessary Strength reduces the penalty to a -1 circumstance penalty instead of removing it entirely.

**Source:** `= this.source` (`= this.source-type`)
