---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Given as thanks for honoring the memories of three unfortunate travelers who met a tragic end in the Willowshore Hinterlands, this red-hooded cloak is decorated with an image of an elaborately dressed performer whose two companions hold a lantern and umbrella for her.

**Activate—Release Lantern** `pf2:3` (concentrate, light, manipulate)

**Frequency** once per day

**Requirements** You don't have the Release Umbrella activation of this cloak active

**Effect** With a wave of the cloak to the left, you cause the image of the lantern-holding companion on the cloak to vanish. A floating red lantern appears at your side and follows you at an arm's length while casting bright light in a 20-foot radius (and dim light for the next 20 feet) like a torch. For 1 hour, while the light from this lantern is active, you gain a +1 item bonus to Diplomacy checks. You can Release Lantern again to dismiss the effect.

> [!danger] Effect: Hongrui's Gratitude (Lantern)

**Activate—Release Umbrella** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You don't have the Release Lantern activation of this cloak active

**Effect** With a wave of the cloak to the right, you cause the image of the umbrella-holding companion on the cloak to vanish. An indestructible red wax paper umbrella appears above you and follows you, shielding you from weather effects, such as rain or bright sunlight. For 1 hour, while this umbrella is active, you gain a +1 item bonus to Survival checks. You can Release Umbrella again to dismiss the effect.

> [!danger] Effect: Hongrui's Gratitude (Umbrella)

**Source:** `= this.source` (`= this.source-type`)
