---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Candlaron the Sculptor is one of Kyonin's most storied and honored wizards. While his final fate is unknown, his greatest creations, the aiudara, remain behind as a legacy of his power—as do other potent items, such as the *Guiding Star Orb*, a navigational traveling aid that the heroic wizard often relied upon when venturing into an unexplored part of the world.

**Activate—Embed Location** 10 minutes (concentrate);

By focusing on the *Guiding Star Orb*, you embed your current location in the item. Thereafter, anyone who holds the *Guiding Star Orb* while Casting a Spell with the teleportation trait to travel to this location arrives precisely, without any inaccuracy at all. The *Guiding Star Orb* can only have one location embedded at a time; if you use this activity a second time, the new location replaces the previous one.

**Activate—Momentary Aiudara** 10 minutes (concentrate, manipulate, teleportation)

**Frequency** once per day

**Effect** You cause a shimmering magical archway to appear next to you as the *Guiding Star Orb* casts a 7th-rank [[Teleport]] to your specifications. If you are teleporting to an aiudara you've visited before, you and the targets appear precisely at that location.

**Source:** `= this.source` (`= this.source-type`)
