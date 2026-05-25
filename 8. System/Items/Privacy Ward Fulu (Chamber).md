---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 120}"
usage: "affixed-to-wall"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fulu seeks to keep thieves, spies, and unwanted attention away from a room. A depiction of a lock appears in the center of this fulu, which is in turn surrounded by circles of broken keys. When applied to a wall inside a room, all creatures within the room gain an item bonus to Stealth checks against creatures outside the room.

The fulu can shield a room of up to 90 square feet, grants a +2 item bonus, and has a duration of 24 hours. If you become [[Hidden]] within the room, you automatically become undetected to creatures of the fulu's level or lower.

**Source:** `= this.source` (`= this.source-type`)
