---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]", "[[Propulsive]]"]
price: "{'gp': 155}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made of shiny brown leather, this *+1 striking sling* has a single white thread interwoven into its cord.

**Activate—Unleash Roar** `pf2:2` (manipulate, sonic)

**Frequency** once per day

**Effect** You pull the white thread free, then whirl the sling in circles at high speed. It lets out an ear-piercing wave of sound. Each creature in a @Template[cone|distance:30] takes @Damage[4d6[sonic]|options:area-damage] damage (DC 21 [[Fortitude]] save). Any creature that fails is [[Deafened]] for 1 round, or 1 hour on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
