---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 900}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These brightly colored, soft-soled boots motivate you to perform risky stunts and grant you the agility to succeed. The boots grant you a +2 item bonus to Acrobatics checks and a +1 circumstance bonus to checks to `act tumble-through` an enemy's space.

The boots can grip solid surfaces and help you avoid a fall, allowing you to use the `act grab-an-edge` reaction even if your hands aren't free. You treat falls as 10 feet shorter or, if you have the [[Cat Fall]] feat, treat your proficiency rank in Acrobatics as one degree better to determine the benefits of that feat. If you have Cat Fall and are already legendary in Acrobatics, you can choose the speed of your fall, from 60 feet per round up to normal falling speed.

**Source:** `= this.source` (`= this.source-type`)
