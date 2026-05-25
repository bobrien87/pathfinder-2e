---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Teleportation]]"]
price: "{'gp': 450}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking ghost touch crossbow* has an array of crystalline lenses and silver fittings along the stock and feels strangely light.

**Activate—Ethereal Vision** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** You aim through the crossbow's crystalline lenses, gaining imprecise vision onto the Ethereal Plane with a range of 60 feet in addition to your normal senses until the end of your turn. You can sense through objects in the Universe this way, and the sense is precise for detecting creatures. Because this sense detects spiritual energy, a creature that's immune to spirit can't be detected in this way.

**Activate—Ethereal Shot** `pf2:1`

**Requirements** Ethereal Vision is active

**Effect** You Strike with the *spiritsight crossbow*. This shot travels through the Ethereal Plane, allowing it to pass through and ignore cover from physical objects within the range of your Ethereal Vision.

**Source:** `= this.source` (`= this.source-type`)
