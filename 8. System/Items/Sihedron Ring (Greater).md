---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2000}"
usage: "worn"
bulk: "—"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Though simple in appearance, Sihedron rings are among the most treasured tokens a runelord would bestow on an agent in times past. Like the more common Sihedron medallion, Sihedron rings created by the original runelords allow for easier scrying of and speaking through those who wear them; Sihedron rings created in modern times don't have this disadvantage.

As long as it's invested, a Sihedron ring protects its wearer from environmental extremes, rendering them immune to severe cold and heat. The ring also grants a +2 status bonus to AC against attacks made during reactions.

**Activate—Costume Change** `pf2:1` (concentrate)

**Effect** You change the shape and appearance of any armor or clothing you wear to appear as ordinary or fancy clothing or armor of your imagining. The actual statistics for what you're wearing doesn't change. Only a creature that's benefiting from truesight or a similar effect can attempt to disbelieve this illusion, with a DC of 29.

**Source:** `= this.source` (`= this.source-type`)
