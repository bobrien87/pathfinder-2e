---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Clockwork]]", "[[Steam]]"]
price: "{'gp': 6000}"
usage: "wornbackpack"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The steamflight pack allows its user to fly without using magic or wings. Each steamflight pack looks like a large brass backpack with two large nozzles mounted on the sides pointing downward. It also features metal arms reaching around the front that terminate in handles with activation buttons on them. When the user holds down an activation button, a complex series of mechanisms pumps water from the large tank in the backpack and releases it through the nozzles as powerful jets of steam, enabling the user to fly short distances. Tilting the handle adjusts the nozzles' angles, allowing the user to control the direction of their flight.

When active, the steamflight pack gives the user a fly Speed of 20 feet. It carries enough water for 20 minutes of operation and can be refilled in five minutes with a supply of normal water and a funnel.

**Activate—On/Off Switch** `pf2:2` (manipulate)

**Effect** You turn the steamflight pack on or off.

**Source:** `= this.source` (`= this.source-type`)
