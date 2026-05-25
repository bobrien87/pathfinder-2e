---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 30}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (concentrate)

**Requirements** You're trained in Athletics

This metal grasshopper studded with emeralds is usually clasped to the legs of a suit of armor.

When you activate it, make a [[Leap]], traveling up to 40 feet horizontally and up to 10 feet vertically.

If you don't end your jump on solid ground, you flutter in the air until the end of your turn, then fall harmlessly at a rate of 60 feet per round until you reach the ground.

**Source:** `= this.source` (`= this.source-type`)
