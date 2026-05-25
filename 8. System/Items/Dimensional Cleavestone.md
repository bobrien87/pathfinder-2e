---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 900, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The edges of this irregular hunk of obsidian seem to shimmer. While wielding a weapon under the effect of a *dimensional cleavestone*, you gain the Tear Rift action for 1 minute.

**Tear Rift** `pf2:2` (magical, manipulate, teleportation)

You carve a rent in space in an adjacent square, choosing another square within 30 feet to connect with your rift. A visible slash appears in both locations, displaying the view from the other side.

Until the end of your next turn, these two squares are treated as adjacent to each other; for example, creatures could Stride or be Shoved through the rifts to their other side, and a creature adjacent to one rift can Strike a creature adjacent to the other.

When Tearing a Rift, you can choose to Step through the rift as part of the activity. The rifts don't automatically pull creatures or objects through, as they take up only a small amount of space within the square, and a creature sharing a space with a rift is unaffected except for determining adjacency. You can have only one rift active at a time.

**Source:** `= this.source` (`= this.source-type`)
