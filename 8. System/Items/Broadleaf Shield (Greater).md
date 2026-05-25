---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 675}"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Though it resembles an enormous leaf freshly plucked from a tree, a *broadleaf shield* is extremely durable. It also regrows rapidly, fully repairing itself when broken if it's left in sunlight for 10 consecutive minutes.

At each dawn, the leaf transforms to an appearance appropriate for the season. While you're wielding the shield, you gain resistance 4 to a damage type depending on the shield's color. This resistance doubles while you have the shield raised.

- **Pink** (void resistance) In spring, the leaf is a delicate blossom-like pink and exudes the energy of life.

- **Green** (fire resistance) In summer, the leaf is a deep, rich green with a waxy coating.

- **Orange** (poison resistance) In autumn, the leaf turns orange, red, or yellow and dehydrates slightly.

- **Brown** (cold resistance) In winter, the leaf turns dead, dry, and brown.

**Activate - Change Season** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The shield transforms as though living through seasons in a moment, becoming the color of your choice for 5 minutes.

**Source:** `= this.source` (`= this.source-type`)
