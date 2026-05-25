---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Comfort]]"]
price: "{'gp': 480}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 padded armor* enables you to hover above the ground and either drift with the wind or be pulled along by another creature or vehicle.

**Activate—Inflate** 10 minutes (air, manipulate)

**Frequency** once per day

**Effect** A gas-filled balloon pops out of the back of your armor and begins to inflate. It takes 10 minutes for the balloon to fully inflate and lift you and up to 5 additional Bulk 5 feet off the ground. By taking another 10 minutes, this balloon can be deflated and properly stowed in the back of your armor. Once inflated, you can spend an action that has the manipulate and move traits to adjust the height you are hovering up or down by up to 20 feet each time. If the balloon takes damage (AC 10, Hardness 0), it will quickly deflate and cause you to fall to the ground. The balloon magically repairs itself at the start of each day.

**Source:** `= this.source` (`= this.source-type`)
