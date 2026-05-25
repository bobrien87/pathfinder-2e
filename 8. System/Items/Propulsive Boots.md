---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These sleek red boots make your legs feel like they're bursting with energy. You gain a +5-foot item bonus to your land Speed and to any climb or swim Speeds you have.

**Activate—Quickening Stomp** A (manipulate)

**Frequency** once per day

**Effect** You stomp three times and gain the [[Quickened]] condition for 1 minute. You can use the extra action to Stride, [[Climb]], or [[Swim]]. (You must still attempt an Athletics check for the Climb and Swim actions unless you have the appropriate movement type.)

**Source:** `= this.source` (`= this.source-type`)
