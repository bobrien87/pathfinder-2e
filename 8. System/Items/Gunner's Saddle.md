---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 20}"
usage: "wornsaddle"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Developed by marauders from the Mana Wastes, this clockwork saddle comes with a retractable weapon mount that can be used as a tripod to stabilize a weapon with the kickback trait. Just like a normal tripod, you Interact to deploy the tripod to stabilize the firearm, and then again to retract the tripod to move it. The saddle uses complex hydraulics to protect the steed from the firearm's recoil.

**Source:** `= this.source` (`= this.source-type`)
