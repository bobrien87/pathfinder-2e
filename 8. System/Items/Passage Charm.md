---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]", "[[Shadow]]"]
price: "{'gp': 1000}"
usage: "worn"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This glossy black brooch is made of solidified shadows and is a gift, given by Avathrael Realmshaper to their allies to allow them to navigate the heart of the forest within Gloaming Arbor. While wearing a *passage charm*, you can cast [[Darkness]] as an innate occult spell twice per day.

**Activate—Shape the Shadows** `pf2:3` (manipulate)

**Frequency** once per day

**Requirements** You're in an area that's dark or dim light

**Effect** You command the shadows to do your bidding, forming a path, a ramp, a wall, or stairs. The *passage charm* casts 5th-rank [[Wall of Stone]], except the spell loses the earth trait, gains the shadow trait, and has a duration of 24 hours, and the wall is created from solid shadows, rather than stone. If any section of the wall is exposed to bright light, that portion of the wall has its Hardness temporarily reduced by half (to Hardness 7).

**Source:** `= this.source` (`= this.source-type`)
