---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Structure]]"]
price: "{'gp': 880}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Before activation, this item appears to be nothing more than a simple rolled-up tent, barely large enough to fit four Medium creatures. Despite attempts to clean it, the tent is perpetually smudged with dirt in various places.

**Activate—Unroll** (10 minutes) (manipulate)

**Frequency** once per day

**Effect** The rolled-up tent expands into a spacious yurt complete with a fire pit, 10 bedrolls, various cooking utensils, and basic food and water.

The yurt can house and feed you and up to nine other Medium creatures that eat roughly as much as a human does; they need not attempt a Survival check to Subsist when you use the yurt. Fires and light inside the yurt do not extend illumination into the area surrounding the yurt, making it harder to spot from a distance.

A large loop of red cloth hangs from one wall. If this loop is pulled, which takes an Interact action, the entire yurt immediately folds back up into its deactivated form, ready for further travel.

**Source:** `= this.source` (`= this.source-type`)
