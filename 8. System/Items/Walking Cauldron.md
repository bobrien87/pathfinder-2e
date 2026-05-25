---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 12}"
usage: "other"
bulk: "4"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This iron cauldron stands upon sturdy iron crow's feet. A *walking cauldron* has a land Speed of 25 feet and can be used as a suitable tool to *Craft* potions, oils, or other liquids.

As a single action, which has the *auditory* and *concentrate* traits, you can command the cauldron to either follow you or to stand in place. When following you, the cauldron does its best to remain within 30 feet of you, but its ungainly movements are too imprecise to predictably direct in a combat encounter or other situation where seconds and precise locations count. It can carry up to 2 Bulk of ingredients for potions or other liquids inside of itself while following you, but if overloaded or if you put anything else inside it, it stands in place and refuses to move until 10 minutes after you remove the excess.

**Source:** `= this.source` (`= this.source-type`)
