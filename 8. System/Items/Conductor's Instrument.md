---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item can be found in the form of any variety of handheld musical instruments. The instrument grants you a +1 item bonus to Performance checks while playing music with it. Once per day, you can use the following activity.

**Activate—Command Performance** `pf2:2` (manipulate) You play a special tune on the instrument, causing it to cast a DC 17 [[Command]] bard spell.

**Source:** `= this.source` (`= this.source-type`)
