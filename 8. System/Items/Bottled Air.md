---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Air]]", "[[Magical]]"]
price: "{'gp': 320}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Appearing to be an ordinary corked glass bottle, this item contains a limitless supply of fresh air. You must uncork the bottle with an Interact action before you can activate it.

**Activate—Breathe In** `pf2:1` (manipulate)

**Effect** You draw a breath of air from the bottle. This allows you to breathe even in an airless or toxic environment. Air doesn't escape the mouth of the bottle, so leaving the open bottle in an airless environment doesn't change the environment.

**Source:** `= this.source` (`= this.source-type`)
