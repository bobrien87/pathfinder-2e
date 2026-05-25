---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Clockwork]]", "[[Magical]]"]
price: "{'gp': 475}"
usage: "worn"
bulk: "3"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This clockwork traveler's chair is shaped like a wheeled frog, with springs attached to the bottom and an extensible tongue on the front.

**Activate—Frog Hop** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You activate the wheelchair's springs to make hopping leaps. For 1 minute, whenever you [[Leap]] with the wheelchair, you can jump 30 feet in any direction without touching the ground. You must land on a space of solid ground within 30 feet of you, or else you fall after using your next action.

**Activate—Grrrabbit!** `pf2:1` (manipulate)

**Frequency** once per minute

**Effect** You activate the wheelchair's tongue to grab a nearby object and bring it to you. [[Interact]] to pick up an unattended object within 15 feet and bring it to your empty hand. If you don't have a hand to take the object, it falls in your space instead.

**Source:** `= this.source` (`= this.source-type`)
